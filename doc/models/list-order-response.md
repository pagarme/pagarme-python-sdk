
# List Order Response

Response object for listing order objects

## Structure

`ListOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetOrderResponse]`](../../doc/models/get-order-response.md) | Optional | The order object |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.list_order_response import ListOrderResponse

list_order_response = ListOrderResponse(
    data=[
        None
    ],
    paging=None
)
```

