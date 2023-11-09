
# Get Voucher Transaction Response

Response for voucher transactions

## Structure

`GetVoucherTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | Text that will appear on the voucher's statement |
| `acquirer_name` | `str` | Optional | Acquirer name |
| `acquirer_affiliation_code` | `str` | Optional | Acquirer affiliation code |
| `acquirer_tid` | `str` | Optional | Acquirer TID |
| `acquirer_nsu` | `str` | Optional | Acquirer NSU |
| `acquirer_auth_code` | `str` | Optional | Acquirer authorization code |
| `acquirer_message` | `str` | Optional | acquirer_message |
| `acquirer_return_code` | `str` | Optional | Acquirer return code |
| `operation_type` | `str` | Optional | Operation type |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | Card data |

## Example (as JSON)

```json
{
  "gateway_id": "gateway_id8",
  "amount": 40,
  "status": "status6",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "statement_descriptor": "statement_descriptor6",
  "acquirer_name": "acquirer_name0",
  "acquirer_affiliation_code": "acquirer_affiliation_code2",
  "acquirer_tid": "acquirer_tid4",
  "acquirer_nsu": "acquirer_nsu4"
}
```

