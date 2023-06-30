
# Get Balance Operation Response

Generic response object for getting a BalanceOperation.

## Structure

`GetBalanceOperationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `status` | `string` | Optional | - |
| `balance_amount` | `string` | Optional | - |
| `balance_old_amount` | `string` | Optional | - |
| `mtype` | `string` | Optional | - |
| `amount` | `string` | Optional | - |
| `fee` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `movement_object` | [`GetMovementObjectBaseResponse`](../../doc/models/get-movement-object-base-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "status": "status8",
  "balance_amount": "balance_amount0",
  "balance_old_amount": "balance_old_amount2",
  "type": "type0"
}
```

