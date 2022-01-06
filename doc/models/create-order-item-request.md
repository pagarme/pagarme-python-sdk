
# Create Order Item Request

Request for creating an order item

## Structure

`CreateOrderItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Amount |
| `description` | `string` | Required | Description |
| `quantity` | `int` | Required | Quantity |
| `category` | `string` | Required | Category |
| `code` | `string` | Optional | The item code passed by the client |

## Example (as JSON)

```json
{
  "amount": 46,
  "description": "description0",
  "quantity": 68,
  "category": "category2",
  "code": null
}
```

