
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
  "gateway_id": "gateway_id4",
  "amount": 24,
  "status": "status2",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "transaction_type": "voucher",
  "statement_descriptor": "statement_descriptor0",
  "acquirer_name": "acquirer_name4",
  "acquirer_affiliation_code": "acquirer_affiliation_code8",
  "acquirer_tid": "acquirer_tid0",
  "acquirer_nsu": "acquirer_nsu0"
}
```

