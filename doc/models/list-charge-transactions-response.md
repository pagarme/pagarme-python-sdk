
# List Charge Transactions Response

Response object for listing charge transactions

## Structure

`ListChargeTransactionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetTransactionResponse]`](../../doc/models/get-transaction-response.md) | Optional | The charge transactions objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.list_charge_transactions_response import ListChargeTransactionsResponse

list_charge_transactions_response = ListChargeTransactionsResponse(
    data=[
        None,
        ,
        
    ],
    paging=None
)
```

