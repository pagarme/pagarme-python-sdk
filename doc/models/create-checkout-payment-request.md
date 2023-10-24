
# Create Checkout Payment Request

Checkout payment request

## Structure

`CreateCheckoutPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepted_payment_methods` | `List[str]` | Required | Accepted Payment Methods |
| `accepted_multi_payment_methods` | `List[object]` | Required | Accepted Multi Payment Methods |
| `success_url` | `str` | Required | Success url |
| `default_payment_method` | `str` | Optional | Default payment method |
| `gateway_affiliation_id` | `str` | Optional | Gateway Affiliation Id |
| `credit_card` | [`CreateCheckoutCreditCardPaymentRequest`](../../doc/models/create-checkout-credit-card-payment-request.md) | Optional | Credit Card payment request |
| `debit_card` | [`CreateCheckoutDebitCardPaymentRequest`](../../doc/models/create-checkout-debit-card-payment-request.md) | Optional | Debit Card payment request |
| `boleto` | [`CreateCheckoutBoletoPaymentRequest`](../../doc/models/create-checkout-boleto-payment-request.md) | Optional | Boleto payment request |
| `customer_editable` | `bool` | Optional | Customer is editable? |
| `expires_in` | `int` | Optional | Time in minutes for expiration |
| `skip_checkout_success_page` | `bool` | Required | Skip postpay success screen? |
| `billing_address_editable` | `bool` | Required | Billing Address is editable? |
| `billing_address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | Billing Address |
| `bank_transfer` | [`CreateCheckoutBankTransferRequest`](../../doc/models/create-checkout-bank-transfer-request.md) | Optional | Bank Transfer payment request |
| `accepted_brands` | `List[str]` | Required | Accepted Brands |
| `pix` | [`CreateCheckoutPixPaymentRequest`](../../doc/models/create-checkout-pix-payment-request.md) | Optional | Pix payment request |

## Example (as JSON)

```json
{
  "accepted_payment_methods": [
    "accepted_payment_methods9",
    "accepted_payment_methods0"
  ],
  "accepted_multi_payment_methods": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "success_url": "success_url8",
  "default_payment_method": "default_payment_method6",
  "gateway_affiliation_id": "gateway_affiliation_id2",
  "credit_card": {
    "statement_descriptor": "statement_descriptor8",
    "installments": [
      {
        "number": 164,
        "total": 16
      }
    ],
    "authentication": {
      "type": "type2",
      "threed_secure": {
        "mpi": "mpi0",
        "cavv": "cavv8",
        "eci": "eci2",
        "transaction_id": "transaction_id0",
        "success_url": "success_url4",
        "ds_transaction_id": "ds_transaction_id0"
      }
    },
    "capture": false
  },
  "debit_card": {
    "statement_descriptor": "statement_descriptor4",
    "authentication": {
      "type": "type2",
      "threed_secure": {
        "mpi": "mpi0",
        "cavv": "cavv8",
        "eci": "eci2",
        "transaction_id": "transaction_id0",
        "success_url": "success_url4",
        "ds_transaction_id": "ds_transaction_id0"
      }
    }
  },
  "boleto": {
    "bank": "bank8",
    "instructions": "instructions2",
    "due_at": "2016-03-13T12:52:32.123Z"
  },
  "skip_checkout_success_page": false,
  "billing_address_editable": false,
  "billing_address": {
    "street": "street8",
    "number": "number4",
    "zip_code": "zip_code2",
    "neighborhood": "neighborhood4",
    "city": "city2",
    "state": "state6",
    "country": "country2",
    "complement": "complement6",
    "metadata": {
      "key0": "metadata5",
      "key1": "metadata6"
    },
    "line_1": "line_18",
    "line_2": "line_26"
  },
  "accepted_brands": [
    "accepted_brands2",
    "accepted_brands3"
  ]
}
```

