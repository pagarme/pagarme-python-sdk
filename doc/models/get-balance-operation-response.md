
# Get Balance Operation Response

Generic response object for getting a BalanceOperation.

## Structure

`GetBalanceOperationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `balance_amount` | `str` | Optional | - |
| `balance_old_amount` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `amount` | `int` | Optional | - |
| `fee` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `movement_object` | [`GetMovementObjectBaseResponse`](../../doc/models/get-movement-object-base-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "status": "status2",
  "balance_amount": "balance_amount0",
  "balance_old_amount": "balance_old_amount8",
  "type": "type0"
}
```

