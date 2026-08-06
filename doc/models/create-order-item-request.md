
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

## Example

```python
from pagarmeapisdk.models.create_order_item_request import CreateOrderItemRequest

create_order_item_request = CreateOrderItemRequest(
    amount=230,
    description='description6',
    quantity=140,
    category='category8',
    code='code2'
)
```

