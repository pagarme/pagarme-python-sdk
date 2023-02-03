
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
  "gateway_id": null,
  "amount": null,
  "status": null,
  "success": null,
  "created_at": null,
  "updated_at": null,
  "attempt_count": null,
  "max_attempts": null,
  "splits": null,
  "next_attempt": null,
  "transaction_type": "boleto",
  "id": null,
  "gateway_response": null,
  "antifraud_response": null,
  "metadata": null,
  "split": null,
  "interest": null,
  "fine": null,
  "max_days_to_pay_past_due": null,
  "url": null,
  "barcode": null,
  "nosso_numero": null,
  "bank": null,
  "document_number": null,
  "instructions": null,
  "billing_address": null,
  "due_at": null,
  "qr_code": null,
  "line": null,
  "pdf_password": null,
  "pdf": null,
  "paid_at": null,
  "paid_amount": null,
  "type": null,
  "credit_at": null,
  "statement_descriptor": null
}
```

