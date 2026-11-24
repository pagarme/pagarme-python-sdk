"""Offline regressions for model imports, nested responses, and Basic Auth."""

import importlib
import subprocess
import sys
import unittest

from base64 import b64decode
from unittest.mock import patch


class ImportRegressionTests(unittest.TestCase):
    def run_fresh_python(self, source):
        result = subprocess.run(
            [sys.executable, "-c", source],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            timeout=60,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_client_imports_in_a_fresh_interpreter(self):
        self.run_fresh_python(
            "from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient"
        )

    def test_each_circular_model_can_be_imported_first(self):
        modules = [
            "get_address_response",
            "get_customer_response",
            "get_plan_item_response",
            "get_plan_response",
            "get_bank_account_response",
            "get_recipient_response",
            "get_discount_response",
            "get_increment_response",
            "get_period_response",
            "get_subscription_item_response",
            "get_subscription_response",
            "get_charge_response",
            "get_invoice_response",
            "get_order_response",
        ]
        for module in modules:
            with self.subTest(module=module):
                self.run_fresh_python(
                    "import importlib; importlib.import_module(%r)"
                    % ("pagarmeapisdk.models." + module)
                )

    def test_all_sdk_modules_import_without_network_access(self):
        self.run_fresh_python(
            "import importlib, pkgutil, pagarmeapisdk\n"
            "from unittest.mock import patch\n"
            "with patch('requests.sessions.Session.send', "
            "side_effect=AssertionError('Unexpected network access')):\n"
            "    for module in pkgutil.walk_packages("
            "pagarmeapisdk.__path__, pagarmeapisdk.__name__ + '.'):\n"
            "        importlib.import_module(module.name)\n"
        )


class NestedResponseTests(unittest.TestCase):
    def model(self, module, name, payload):
        imported = importlib.import_module("pagarmeapisdk.models." + module)
        return getattr(imported, name).from_dictionary(payload)

    def test_customer_address_back_references_preserve_nested_data(self):
        response = self.model(
            "get_customer_response",
            "GetCustomerResponse",
            {
                "id": "cus_root",
                "address": {"id": "addr_root", "customer": {"id": "cus_nested"}},
            },
        )
        self.assertEqual(response.address.customer.id, "cus_nested")
        response = self.model(
            "get_address_response",
            "GetAddressResponse",
            {
                "id": "addr_root",
                "customer": {"id": "cus_root", "address": {"id": "addr_nested"}},
            },
        )
        self.assertEqual(response.customer.address.id, "addr_nested")

    def test_bank_account_recipient_back_reference(self):
        response = self.model(
            "get_bank_account_response",
            "GetBankAccountResponse",
            {
                "id": "ba_root",
                "recipient": {
                    "id": "re_root",
                    "default_bank_account": {"id": "ba_nested"},
                },
            },
        )
        self.assertEqual(response.recipient.default_bank_account.id, "ba_nested")

    def test_plan_item_back_reference(self):
        response = self.model(
            "get_plan_item_response",
            "GetPlanItemResponse",
            {
                "id": "pi_root",
                "plan": {"id": "plan_root", "items": [{"id": "pi_nested"}]},
            },
        )
        self.assertEqual(response.plan.items[0].id, "pi_nested")

    def test_charge_invoice_order_back_references(self):
        response = self.model(
            "get_charge_response",
            "GetChargeResponse",
            {
                "id": "ch_root",
                "invoice": {"id": "in_root", "charge": {"id": "ch_invoice"}},
                "order": {"id": "or_root", "charges": [{"id": "ch_order"}]},
            },
        )
        self.assertEqual(response.invoice.charge.id, "ch_invoice")
        self.assertEqual(response.order.charges[0].id, "ch_order")

    def test_subscription_discounts_increments_periods_and_items(self):
        response = self.model(
            "get_subscription_response",
            "GetSubscriptionResponse",
            {
                "id": "sub_root",
                "current_cycle": {
                    "id": "cycle_root",
                    "subscription": {"id": "sub_cycle"},
                },
                "items": [{"id": "si_root", "subscription": {"id": "sub_item"}}],
                "discounts": [
                    {
                        "id": "di_root",
                        "subscription": {"id": "sub_discount"},
                        "subscription_item": {"id": "si_discount"},
                    }
                ],
                "increments": [
                    {
                        "id": "inc_root",
                        "subscription": {"id": "sub_increment"},
                        "subscription_item": {"id": "si_increment"},
                    }
                ],
            },
        )
        self.assertEqual(response.current_cycle.subscription.id, "sub_cycle")
        self.assertEqual(response.items[0].subscription.id, "sub_item")
        self.assertEqual(response.discounts[0].subscription.id, "sub_discount")
        self.assertEqual(response.discounts[0].subscription_item.id, "si_discount")
        self.assertEqual(response.increments[0].subscription.id, "sub_increment")
        self.assertEqual(response.increments[0].subscription_item.id, "si_increment")


class BasicAuthTests(unittest.TestCase):
    def test_empty_password_is_valid_and_builds_the_expected_header(self):
        from pagarmeapisdk.http.auth.basic_auth import BasicAuth, BasicAuthCredentials
        from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient
        import requests

        captured = []

        def send(session, request, **kwargs):
            captured.append(request)
            response = requests.Response()
            response.status_code = 200
            response._content = b'{"id": "cus_unit"}'
            response.headers["Content-Type"] = "application/json"
            response.request = request
            return response

        credentials = BasicAuthCredentials(username="sk_test_unit", password="")
        self.assertTrue(BasicAuth(credentials).is_valid())
        with requests.Session() as session:
            client = PagarmeapisdkClient(
                basic_auth_credentials=credentials,
                http_client_instance=session,
                override_http_client_configuration=True,
                max_retries=0,
            )
            with patch(
                "requests.sessions.Session.send", autospec=True, side_effect=send
            ):
                response = client.customers.get_customer(customer_id="cus_unit")
        self.assertEqual(response.id, "cus_unit")
        self.assertEqual(len(captured), 1)
        scheme, encoded = captured[0].headers["Authorization"].split(" ", 1)
        self.assertEqual(scheme, "Basic")
        self.assertEqual(b64decode(encoded), b"sk_test_unit:")

    def test_non_empty_password_remains_supported(self):
        from pagarmeapisdk.http.auth.basic_auth import BasicAuth, BasicAuthCredentials

        self.assertTrue(
            BasicAuth(BasicAuthCredentials("username", "password")).is_valid()
        )

    def test_missing_credentials_or_empty_username_are_invalid(self):
        from pagarmeapisdk.http.auth.basic_auth import BasicAuth, BasicAuthCredentials

        self.assertFalse(BasicAuth(None).is_valid())
        self.assertFalse(BasicAuth(BasicAuthCredentials("", "")).is_valid())
        with self.assertRaises(ValueError):
            BasicAuthCredentials("username", None)

    def test_cloning_can_explicitly_replace_a_password_with_an_empty_string(self):
        from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials

        original = BasicAuthCredentials("username", "password")
        cloned = original.clone_with(password="")
        self.assertEqual(cloned.username, "username")
        self.assertEqual(cloned.password, "")
        self.assertEqual(original.password, "password")
        self.assertEqual(original.clone_with().password, "password")

    def test_environment_accepts_an_explicit_empty_password(self):
        from pagarmeapisdk.http.auth.basic_auth import BasicAuth, BasicAuthCredentials

        with patch.dict(
            "os.environ", {"USERNAME": "sk_test_unit", "PASSWORD": ""}, clear=True
        ):
            credentials = BasicAuthCredentials.from_environment()
        self.assertIsNotNone(credentials)
        self.assertTrue(BasicAuth(credentials).is_valid())


if __name__ == "__main__":
    unittest.main()
