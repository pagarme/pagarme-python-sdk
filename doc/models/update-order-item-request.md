
# Update Order Item Request

Update Order item Request

## Structure

`UpdateOrderItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | - |
| `description` | `str` | Required | - |
| `quantity` | `int` | Required | - |
| `category` | `str` | Required | - |

## Example

```python
from pagarmeapisdk.models.update_order_item_request import UpdateOrderItemRequest

update_order_item_request = UpdateOrderItemRequest(
    amount=234,
    description='description4',
    quantity=92,
    category='category2'
)
```

