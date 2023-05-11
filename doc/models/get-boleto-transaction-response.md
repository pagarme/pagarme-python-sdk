
# Get Boleto Transaction Response

Response object for getting a boleto transaction

## Structure

`GetBoletoTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `string` | Optional | - |
| `barcode` | `string` | Optional | - |
| `nosso_numero` | `string` | Optional | - |
| `bank` | `string` | Optional | - |
| `document_number` | `string` | Optional | - |
| `instructions` | `string` | Optional | - |
| `billing_address` | [`GetBillingAddressResponse`](../../doc/models/get-billing-address-response.md) | Optional | - |
| `due_at` | `datetime` | Optional | - |
| `qr_code` | `string` | Optional | - |
| `line` | `string` | Optional | - |
| `pdf_password` | `string` | Optional | - |
| `pdf` | `string` | Optional | - |
| `paid_at` | `datetime` | Optional | - |
| `paid_amount` | `string` | Optional | - |
| `mtype` | `string` | Optional | - |
| `credit_at` | `datetime` | Optional | - |
| `statement_descriptor` | `string` | Optional | Soft Descriptor |

## Example (as JSON)

```json
{
  "gateway_id": "gateway_id4",
  "amount": 250,
  "status": "status2",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "transaction_type": "boleto",
  "url": "url4",
  "barcode": "barcode0",
  "nosso_numero": "nosso_numero0",
  "bank": "bank8",
  "document_number": "document_number6"
}
```

