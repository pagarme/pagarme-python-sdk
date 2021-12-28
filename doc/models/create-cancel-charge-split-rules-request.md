
# Create Cancel Charge Split Rules Request

Creates a refund with split rules

## Structure

`CreateCancelChargeSplitRulesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | The split rule gateway id |
| `amount` | `int` | Required | The split rule amount |
| `mtype` | `string` | Required | The amount type (flat ou percentage) |

## Example (as JSON)

```json
{
  "id": "id0",
  "Amount": 156,
  "type": "type0"
}
```

