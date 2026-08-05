
# List Usages Response

Response model for listing the usages from a subscription item

## Structure

`ListUsagesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetUsageResponse]`](../../doc/models/get-usage-response.md) | Optional | The usage objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_usage_response import GetUsageResponse
from pagarmeapisdk.models.list_usages_response import ListUsagesResponse

list_usages_response = ListUsagesResponse(
    data=[
        None,
        GetUsageResponse(),
        GetUsageResponse()
    ],
    paging=None
)
```

