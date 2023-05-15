
# Get Private Label Transaction Response

Response object for getting a private label transaction

## Structure

`GetPrivateLabelTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `string` | Optional | Text that will appear on the credit card's statement |
| `acquirer_name` | `string` | Optional | Acquirer name |
| `acquirer_affiliation_code` | `string` | Optional | Aquirer affiliation code |
| `acquirer_tid` | `string` | Optional | Acquirer TID |
| `acquirer_nsu` | `string` | Optional | Acquirer NSU |
| `acquirer_auth_code` | `string` | Optional | Acquirer authorization code |
| `operation_type` | `string` | Optional | Operation type |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | Card data |
| `acquirer_message` | `string` | Optional | Acquirer message |
| `acquirer_return_code` | `string` | Optional | Acquirer Return Code |
| `installments` | `int` | Optional | Number of installments |

## Example (as JSON)

```json
{
  "gateway_id": "gateway_id6",
  "amount": 20,
  "status": "status6",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "transaction_type": "private_label",
  "statement_descriptor": "statement_descriptor0",
  "acquirer_name": "acquirer_name4",
  "acquirer_affiliation_code": "acquirer_affiliation_code8",
  "acquirer_tid": "acquirer_tid0",
  "acquirer_nsu": "acquirer_nsu0"
}
```

