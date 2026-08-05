
# List Charges Response

Response object for listing charges

## Structure

`ListChargesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetChargeResponse]`](../../doc/models/get-charge-response.md) | Optional | The charge objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_charge_response import GetChargeResponse
from pagarmeapisdk.models.list_charges_response import ListChargesResponse

list_charges_response = ListChargesResponse(
    data=[
        None,
        GetChargeResponse()
    ],
    paging=None
)
```

