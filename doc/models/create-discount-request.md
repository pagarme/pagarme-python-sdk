
# Create Discount Request

Request for creating a new discount

## Structure

`CreateDiscountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `float` | Required | The discount value |
| `discount_type` | `str` | Required | Discount type. Can be either flat or percentage. |
| `item_id` | `str` | Required | The item where the discount will be applied |
| `cycles` | `int` | Optional | Number of cycles that the discount will be applied |
| `description` | `str` | Optional | Description |

## Example (as JSON)

```json
{
  "value": 146.6,
  "discount_type": "discount_type6",
  "item_id": "item_id2",
  "cycles": 164,
  "description": "description2"
}
```

