
# List Customers Response

Response for listing the customers

## Structure

`ListCustomersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetCustomerResponse]`](../../doc/models/get-customer-response.md) | Optional | The customer object |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.list_customers_response import ListCustomersResponse

list_customers_response = ListCustomersResponse(
    data=[
        None
    ],
    paging=None
)
```

