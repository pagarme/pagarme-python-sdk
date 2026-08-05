
# List Cycles Response

Response object for listing subscription cycles

## Structure

`ListCyclesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetPeriodResponse]`](../../doc/models/get-period-response.md) | Optional | The subscription cycles objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_period_response import GetPeriodResponse
from pagarmeapisdk.models.list_cycles_response import ListCyclesResponse

list_cycles_response = ListCyclesResponse(
    data=[
        None,
        GetPeriodResponse()
    ],
    paging=None
)
```

