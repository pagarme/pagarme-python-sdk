
# List Plans Response

Response object for listing plans

## Structure

`ListPlansResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetPlanResponse]`](../../doc/models/get-plan-response.md) | Optional | The plan objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.list_plans_response import ListPlansResponse

list_plans_response = ListPlansResponse(
    data=[
        None
    ],
    paging=None
)
```

