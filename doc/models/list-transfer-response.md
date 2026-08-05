
# List Transfer Response

List of paginated transfer objects

## Structure

`ListTransferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetTransferResponse]`](../../doc/models/get-transfer-response.md) | Optional | Transfers |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging |

## Example

```python
from pagarmeapisdk.models.list_transfer_response import ListTransferResponse

list_transfer_response = ListTransferResponse(
    data=[
        None
    ],
    paging=None
)
```

