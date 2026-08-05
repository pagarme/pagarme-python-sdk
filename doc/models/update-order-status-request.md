
# Update Order Status Request

## Structure

`UpdateOrderStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Required | Order status |

## Example

```python
from pagarmeapisdk.models.update_order_status_request import UpdateOrderStatusRequest

update_order_status_request = UpdateOrderStatusRequest(
    status='status4'
)
```

