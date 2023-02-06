
# Get Voucher Transaction Response

Response for voucher transactions

## Structure

`GetVoucherTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `string` | Optional | Text that will appear on the voucher's statement |
| `acquirer_name` | `string` | Optional | Acquirer name |
| `acquirer_affiliation_code` | `string` | Optional | Acquirer affiliation code |
| `acquirer_tid` | `string` | Optional | Acquirer TID |
| `acquirer_nsu` | `string` | Optional | Acquirer NSU |
| `acquirer_auth_code` | `string` | Optional | Acquirer authorization code |
| `acquirer_message` | `string` | Optional | acquirer_message |
| `acquirer_return_code` | `string` | Optional | Acquirer return code |
| `operation_type` | `string` | Optional | Operation type |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | Card data |

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
  "transaction_type": "voucher",
  "id": null,
  "gateway_response": null,
  "antifraud_response": null,
  "metadata": null,
  "split": null,
  "interest": null,
  "fine": null,
  "max_days_to_pay_past_due": null,
  "statement_descriptor": null,
  "acquirer_name": null,
  "acquirer_affiliation_code": null,
  "acquirer_tid": null,
  "acquirer_nsu": null,
  "acquirer_auth_code": null,
  "acquirer_message": null,
  "acquirer_return_code": null,
  "operation_type": null,
  "card": null
}
```

