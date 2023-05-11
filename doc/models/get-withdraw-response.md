
# Get Withdraw Response

## Structure

`GetWithdrawResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `gateway_id` | `string` | Optional | - |
| `amount` | `int` | Optional | - |
| `status` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `metadata` | `List of string` | Optional | - |
| `fee` | `int` | Optional | - |
| `funding_date` | `datetime` | Optional | - |
| `funding_estimated_date` | `datetime` | Optional | - |
| `mtype` | `string` | Optional | - |
| `source` | [`GetWithdrawSourceResponse`](../../doc/models/get-withdraw-source-response.md) | Optional | - |
| `target` | [`GetWithdrawTargetResponse`](../../doc/models/get-withdraw-target-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "gateway_id": "gateway_id0",
  "amount": 46,
  "status": "status8",
  "created_at": "2016-03-13T12:52:32.123Z"
}
```

