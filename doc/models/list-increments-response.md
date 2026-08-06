
# List Increments Response

## Structure

`ListIncrementsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetIncrementResponse]`](../../doc/models/get-increment-response.md) | Optional | The Increments response |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_increment_response import GetIncrementResponse
from pagarmeapisdk.models.list_increments_response import ListIncrementsResponse

list_increments_response = ListIncrementsResponse(
    data=[
        None,
        GetIncrementResponse(),
        GetIncrementResponse()
    ],
    paging=None
)
```

