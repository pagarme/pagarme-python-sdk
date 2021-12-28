
# Create Increment Request

Request for creating a new increment

## Structure

`CreateIncrementRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `float` | Required | The increment value |
| `increment_type` | `string` | Required | Increment type. Can be either flat or percentage. |
| `item_id` | `string` | Required | The item where the increment will be applied |
| `cycles` | `int` | Optional | Number of cycles that the increment will be applied |
| `description` | `string` | Optional | Description |

## Example (as JSON)

```json
{
  "value": 251.52,
  "increment_type": "increment_type8",
  "item_id": "item_id0",
  "cycles": null,
  "description": null
}
```

