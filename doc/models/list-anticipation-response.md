
# List Anticipation Response

Anticipations

## Structure

`ListAnticipationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetAnticipationResponse]`](../../doc/models/get-anticipation-response.md) | Optional | Anticipations |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging |

## Example

```python
from pagarmeapisdk.models.get_anticipation_response import GetAnticipationResponse
from pagarmeapisdk.models.list_anticipation_response import ListAnticipationResponse

list_anticipation_response = ListAnticipationResponse(
    data=[
        None,
        GetAnticipationResponse()
    ],
    paging=None
)
```

