
# Get Boleto Transaction Response

Response object for getting a boleto transaction

## Structure

`GetBoletoTransactionResponse`

## Inherits From

[`GetTransactionResponse`](/doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `string` | Required | - |
| `barcode` | `string` | Required | - |
| `nosso_numero` | `string` | Required | - |
| `bank` | `string` | Required | - |
| `document_number` | `string` | Required | - |
| `instructions` | `string` | Required | - |
| `billing_address` | [`GetBillingAddressResponse`](/doc/models/get-billing-address-response.md) | Required | - |
| `due_at` | `datetime` | Optional | - |
| `qr_code` | `string` | Required | - |
| `line` | `string` | Required | - |
| `pdf_password` | `string` | Required | - |
| `pdf` | `string` | Required | - |
| `paid_at` | `datetime` | Optional | - |
| `paid_amount` | `string` | Required | - |
| `mtype` | `string` | Required | - |
| `credit_at` | `datetime` | Optional | - |
| `statement_descriptor` | `string` | Required | Soft Descriptor |

## Example (as JSON)

```json
{
  "url": "url4",
  "barcode": "barcode0",
  "nosso_numero": "nosso_numero0",
  "bank": "bank8",
  "document_number": "document_number6",
  "instructions": "instructions2",
  "billing_address": {
    "street": "street8",
    "number": "number4",
    "zip_code": "zip_code2",
    "neighborhood": "neighborhood4",
    "city": "city2",
    "state": "state6",
    "country": "country2",
    "complement": "complement6",
    "line_1": "line_18",
    "line_2": "line_26"
  },
  "due_at": null,
  "qr_code": "qr_code6",
  "line": "line2",
  "pdf_password": "pdf_password8",
  "pdf": "pdf0",
  "paid_at": null,
  "paid_amount": "paid_amount8",
  "type": "type0",
  "credit_at": null,
  "statement_descriptor": "statement_descriptor0",
  "gateway_id": "gateway_id0",
  "amount": 46,
  "status": "status8",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "updated_at": "2016-03-13T12:52:32.123Z",
  "attempt_count": 70,
  "max_attempts": 174,
  "splits": [
    {
      "type": "type4",
      "amount": 62,
      "recipient": null,
      "gateway_id": "gateway_id4",
      "options": null,
      "id": "id6"
    },
    {
      "type": "type3",
      "amount": 63,
      "recipient": null,
      "gateway_id": "gateway_id3",
      "options": null,
      "id": "id7"
    }
  ],
  "next_attempt": null,
  "transaction_type": null,
  "id": "id0",
  "gateway_response": {
    "code": "code6",
    "errors": [
      {
        "message": "message3"
      },
      {
        "message": "message4"
      },
      {
        "message": "message5"
      }
    ]
  },
  "antifraud_response": {
    "status": "status0",
    "return_code": "return_code8",
    "return_message": "return_message4",
    "provider_name": "provider_name4",
    "score": "score8"
  },
  "metadata": null,
  "split": [
    {
      "type": "type6",
      "amount": 28,
      "recipient": null,
      "gateway_id": "gateway_id6",
      "options": null,
      "id": "id4"
    },
    {
      "type": "type5",
      "amount": 27,
      "recipient": null,
      "gateway_id": "gateway_id5",
      "options": null,
      "id": "id5"
    },
    {
      "type": "type4",
      "amount": 26,
      "recipient": null,
      "gateway_id": "gateway_id4",
      "options": null,
      "id": "id6"
    }
  ]
}
```

