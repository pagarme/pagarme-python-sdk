
# Create Payment Request

Payment data

## Structure

`CreatePaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_method` | `string` | Required | Payment method |
| `credit_card` | [`CreateCreditCardPaymentRequest`](../../doc/models/create-credit-card-payment-request.md) | Optional | Settings for credit card payment |
| `debit_card` | [`CreateDebitCardPaymentRequest`](../../doc/models/create-debit-card-payment-request.md) | Optional | Settings for debit card payment |
| `boleto` | [`CreateBoletoPaymentRequest`](../../doc/models/create-boleto-payment-request.md) | Optional | Settings for boleto payment |
| `currency` | `string` | Optional | Currency. Must be informed using 3 characters |
| `voucher` | [`CreateVoucherPaymentRequest`](../../doc/models/create-voucher-payment-request.md) | Optional | Settings for voucher payment |
| `split` | [`List of CreateSplitRequest`](../../doc/models/create-split-request.md) | Optional | Splits |
| `bank_transfer` | [`CreateBankTransferPaymentRequest`](../../doc/models/create-bank-transfer-payment-request.md) | Optional | Settings for bank transfer payment |
| `gateway_affiliation_id` | `string` | Optional | Gateway affiliation code |
| `amount` | `int` | Optional | The amount of the payment, in cents |
| `checkout` | [`CreateCheckoutPaymentRequest`](../../doc/models/create-checkout-payment-request.md) | Optional | Settings for checkout payment |
| `customer_id` | `string` | Optional | Customer Id |
| `customer` | [`CreateCustomerRequest`](../../doc/models/create-customer-request.md) | Optional | Customer |
| `metadata` | `dict` | Optional | Metadata |
| `cash` | [`CreateCashPaymentRequest`](../../doc/models/create-cash-payment-request.md) | Optional | Settings for cash payment |
| `private_label` | [`CreatePrivateLabelPaymentRequest`](../../doc/models/create-private-label-payment-request.md) | Optional | Settings for private label payment |
| `pix` | [`CreatePixPaymentRequest`](../../doc/models/create-pix-payment-request.md) | Optional | Settings for pix payment |

## Example (as JSON)

```json
{
  "payment_method": "payment_method0",
  "credit_card": {
    "installments": 52,
    "statement_descriptor": "statement_descriptor8",
    "card": {
      "number": "number0",
      "holder_name": "holder_name8",
      "exp_month": 54,
      "exp_year": 242,
      "cvv": "cvv0"
    },
    "card_id": "card_id4",
    "card_token": "card_token2"
  },
  "debit_card": {
    "statement_descriptor": "statement_descriptor4",
    "card": {
      "number": "number0",
      "holder_name": "holder_name8",
      "exp_month": 104,
      "exp_year": 192,
      "cvv": "cvv0"
    },
    "card_id": "card_id0",
    "card_token": "card_token6",
    "recurrence": false
  },
  "boleto": {
    "retries": 226,
    "bank": "bank8",
    "instructions": "instructions2",
    "due_at": "2016-03-13T12:52:32.123Z",
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
        "key0": "metadata5"
      },
      "line_1": "line_18",
      "line_2": "line_26"
    },
    "billing_address_id": "billing_address_id6",
    "nosso_numero": "nosso_numero0",
    "document_number": "document_number6",
    "statement_descriptor": "statement_descriptor0",
    "interest": {
      "days": 160,
      "type": "type0",
      "amount": 234
    },
    "fine": {
      "days": 130,
      "type": "type8",
      "amount": 52
    }
  },
  "currency": "currency0",
  "voucher": {
    "statement_descriptor": "statement_descriptor2",
    "card_id": "card_id8",
    "card_token": "card_token8",
    "Card": {
      "number": "number0",
      "holder_name": "holder_name8",
      "exp_month": 198,
      "exp_year": 238,
      "cvv": "cvv0"
    },
    "recurrency_cycle": "recurrency_cycle6"
  }
}
```

