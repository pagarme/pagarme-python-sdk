
# List Invoices Response

Response object for listing invoices

## Structure

`ListInvoicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetInvoiceResponse]`](../../doc/models/get-invoice-response.md) | Optional | The Invoice objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.list_invoices_response import ListInvoicesResponse

list_invoices_response = ListInvoicesResponse(
    data=[
        None
    ],
    paging=None
)
```

