
# Create Cancel Charge Split Rules Request

Creates a refund with split rules

## Structure

`CreateCancelChargeSplitRulesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The split rule gateway id |
| `amount` | `int` | Required | The split rule amount |
| `mtype` | `str` | Required | The amount type (flat ou percentage) |

## Example (as JSON)

```json
{
  "id": "id6",
  "Amount": 222,
  "type": "type6"
}
```

