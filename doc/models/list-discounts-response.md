
# List Discounts Response

## Structure

`ListDiscountsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetDiscountResponse]`](../../doc/models/get-discount-response.md) | Optional | The Discounts response |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_discount_response import GetDiscountResponse
from pagarmeapisdk.models.list_discounts_response import ListDiscountsResponse

list_discounts_response = ListDiscountsResponse(
    data=[
        None,
        GetDiscountResponse()
    ],
    paging=None
)
```

