
# Get Transaction Response

Generic response object for getting a transaction.

## Structure

`GetTransactionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gateway_id` | `string` | Optional | Gateway transaction id |
| `amount` | `int` | Optional | Amount in cents |
| `status` | `string` | Optional | Transaction status |
| `success` | `bool` | Optional | Indicates if the transaction ocurred successfuly |
| `created_at` | `datetime` | Optional | Creation date |
| `updated_at` | `datetime` | Optional | Last update date |
| `attempt_count` | `int` | Optional | Number of attempts tried |
| `max_attempts` | `int` | Optional | Max attempts |
| `splits` | [`List of GetSplitResponse`](../../doc/models/get-split-response.md) | Optional | Splits |
| `next_attempt` | `datetime` | Optional | Date and time of the next attempt |
| `transaction_type` | `string` | Optional | - |
| `id` | `string` | Optional | Código da transação |
| `gateway_response` | [`GetGatewayResponseResponse`](../../doc/models/get-gateway-response-response.md) | Optional | The Gateway Response |
| `antifraud_response` | [`GetAntifraudResponse`](../../doc/models/get-antifraud-response.md) | Optional | - |
| `metadata` | `dict` | Optional | - |
| `split` | [`List of GetSplitResponse`](../../doc/models/get-split-response.md) | Optional | - |
| `interest` | [`GetInterestResponse`](../../doc/models/get-interest-response.md) | Optional | - |
| `fine` | [`GetFineResponse`](../../doc/models/get-fine-response.md) | Optional | - |
| `max_days_to_pay_past_due` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "gateway_id": "gateway_id0",
  "amount": 46,
  "status": "status8",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "transaction_type": "transaction"
}
```

