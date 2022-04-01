# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.configuration import Server
from pagarmeapisdk.controllers.base_controller import BaseController
from pagarmeapisdk.models.get_invoice_response import GetInvoiceResponse
from pagarmeapisdk.models.list_invoices_response import ListInvoicesResponse


class InvoicesController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config, auth_managers):
        super(InvoicesController, self).__init__(config, auth_managers)

    def create_invoice(self,
                       subscription_id,
                       cycle_id,
                       request=None,
                       idempotency_key=None):
        """Does a POST request to /subscriptions/{subscription_id}/cycles/{cycle_id}/pay.

        Create an Invoice

        Args:
            subscription_id (string): Subscription Id
            cycle_id (string): Cycle Id
            request (CreateInvoiceRequest, optional): TODO: type description
                here.
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/subscriptions/{subscription_id}/cycles/{cycle_id}/pay'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True},
            'cycle_id': {'value': cycle_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetInvoiceResponse.from_dictionary)

        return decoded

    def get_invoices(self,
                     page=None,
                     size=None,
                     code=None,
                     customer_id=None,
                     subscription_id=None,
                     created_since=None,
                     created_until=None,
                     status=None,
                     due_since=None,
                     due_until=None,
                     customer_document=None):
        """Does a GET request to /invoices.

        Gets all invoices

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            code (string, optional): Filter for Invoice's code
            customer_id (string, optional): Filter for Invoice's customer id
            subscription_id (string, optional): Filter for Invoice's
                subscription id
            created_since (datetime, optional): Filter for Invoice's creation
                date start range
            created_until (datetime, optional): Filter for Invoices creation
                date end range
            status (string, optional): Filter for Invoice's status
            due_since (datetime, optional): Filter for Invoice's due date
                start range
            due_until (datetime, optional): Filter for Invoice's due date end
                range
            customer_document (string, optional): TODO: type description
                here.

        Returns:
            ListInvoicesResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/invoices'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'page': page,
            'size': size,
            'code': code,
            'customer_id': customer_id,
            'subscription_id': subscription_id,
            'created_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since),
            'created_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until),
            'status': status,
            'due_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, due_since),
            'due_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, due_until),
            'customer_document': customer_document
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, ListInvoicesResponse.from_dictionary)

        return decoded

    def cancel_invoice(self,
                       invoice_id,
                       idempotency_key=None):
        """Does a DELETE request to /invoices/{invoice_id}.

        Cancels an invoice

        Args:
            invoice_id (string): Invoice id
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/invoices/{invoice_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetInvoiceResponse.from_dictionary)

        return decoded

    def update_invoice_metadata(self,
                                invoice_id,
                                request,
                                idempotency_key=None):
        """Does a PATCH request to /invoices/{invoice_id}/metadata.

        Updates the metadata from an invoice

        Args:
            invoice_id (string): The invoice id
            request (UpdateMetadataRequest): Request for updating the invoice
                metadata
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/invoices/{invoice_id}/metadata'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetInvoiceResponse.from_dictionary)

        return decoded

    def get_partial_invoice(self,
                            subscription_id):
        """Does a GET request to /subscriptions/{subscription_id}/partial-invoice.

        TODO: type endpoint description here.

        Args:
            subscription_id (string): Subscription Id

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/subscriptions/{subscription_id}/partial-invoice'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetInvoiceResponse.from_dictionary)

        return decoded

    def update_invoice_status(self,
                              invoice_id,
                              request,
                              idempotency_key=None):
        """Does a PATCH request to /invoices/{invoice_id}/status.

        Updates the status from an invoice

        Args:
            invoice_id (string): Invoice Id
            request (UpdateInvoiceStatusRequest): Request for updating an
                invoice's status
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/invoices/{invoice_id}/status'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetInvoiceResponse.from_dictionary)

        return decoded

    def get_invoice(self,
                    invoice_id):
        """Does a GET request to /invoices/{invoice_id}.

        Gets an invoice

        Args:
            invoice_id (string): Invoice Id

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/invoices/{invoice_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'invoice_id': {'value': invoice_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetInvoiceResponse.from_dictionary)

        return decoded
