
# List Withdrawals

## Structure

`ListWithdrawals`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetWithdrawResponse]`](../../doc/models/get-withdraw-response.md) | Required | The Increments response |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Required | Paging object |

## Example

```python
from pagarmeapisdk.models.list_withdrawals import ListWithdrawals
from pagarmeapisdk.models.paging_response import PagingResponse

list_withdrawals = ListWithdrawals(
    data=[
        None
    ],
    paging=PagingResponse()
)
```

