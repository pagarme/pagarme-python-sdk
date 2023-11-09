
# Create Order Item Request

Request for creating an order item

## Structure

`CreateOrderItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Amount |
| `description` | `str` | Required | Description |
| `quantity` | `int` | Required | Quantity |
| `category` | `str` | Required | Category |
| `code` | `str` | Optional | The item code passed by the client |

## Example (as JSON)

```json
{
  "amount": 102,
  "description": "description4",
  "quantity": 216,
  "category": "category4",
  "code": "code4"
}
```

