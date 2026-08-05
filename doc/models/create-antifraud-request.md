
# Create Antifraud Request

## Structure

`CreateAntifraudRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | - |
| `clearsale` | [`CreateClearSaleRequest`](../../doc/models/create-clear-sale-request.md) | Required | - |

## Example

```python
from pagarmeapisdk.models.create_antifraud_request import CreateAntifraudRequest
from pagarmeapisdk.models.create_clear_sale_request import CreateClearSaleRequest

create_antifraud_request = CreateAntifraudRequest(
    mtype='type8',
    clearsale=CreateClearSaleRequest(
        custom_sla=None
    )
)
```

