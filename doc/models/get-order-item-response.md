
# Get Order Item Response

Response object for getting an order item

## Structure

`GetOrderItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Id |
| `mtype` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `amount` | `int` | Optional | - |
| `quantity` | `int` | Optional | - |
| `category` | `str` | Optional | Category |
| `code` | `str` | Optional | Code |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_order_item_response import GetOrderItemResponse

get_order_item_response = GetOrderItemResponse(
    id='id4',
    mtype='type6',
    description='description4',
    amount=140,
    quantity=254
)
```

