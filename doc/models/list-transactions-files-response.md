
# List Transactions Files Response

Response object for listing of transactions files

## Structure

`ListTransactionsFilesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetTransactionReportFileResponse]`](../../doc/models/get-transaction-report-file-response.md) | Optional | - |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_transaction_report_file_response import GetTransactionReportFileResponse
from pagarmeapisdk.models.list_transactions_files_response import ListTransactionsFilesResponse

list_transactions_files_response = ListTransactionsFilesResponse(
    data=[
        None,
        GetTransactionReportFileResponse()
    ],
    paging=None
)
```

