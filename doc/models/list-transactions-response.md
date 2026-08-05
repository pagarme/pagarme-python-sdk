
# List Transactions Response

Response object for listing transactions

## Structure

`ListTransactionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetTransactionResponse]`](../../doc/models/get-transaction-response.md) | Optional | The transaction objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.list_transactions_response import ListTransactionsResponse

list_transactions_response = ListTransactionsResponse(
    data=[
        None,
        ,
        
    ],
    paging=None
)
```

