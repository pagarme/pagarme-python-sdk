
# Update Price Bracket Request

Request for updating a price bracket

## Structure

`UpdatePriceBracketRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_quantity` | `int` | Required | Start quantity of the bracket |
| `price` | `int` | Required | Price |
| `end_quantity` | `int` | Optional | End quantity of the bracket |
| `overage_price` | `int` | Optional | Overage price |

## Example (as JSON)

```json
{
  "start_quantity": 154,
  "price": 164,
  "end_quantity": 162,
  "overage_price": 176
}
```

