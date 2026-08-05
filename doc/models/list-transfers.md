
# List Transfers

## Structure

`ListTransfers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetTransfer]`](../../doc/models/get-transfer.md) | Required | The Increments response |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Required | Paging object |

## Example

```python
from pagarmeapisdk.models.list_transfers import ListTransfers
from pagarmeapisdk.models.paging_response import PagingResponse

list_transfers = ListTransfers(
    data=[
        None
    ],
    paging=PagingResponse()
)
```

