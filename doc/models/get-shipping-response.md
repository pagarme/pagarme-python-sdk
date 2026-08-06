
# Get Shipping Response

Response object for getting the shipping data

## Structure

`GetShippingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | - |
| `description` | `str` | Optional | - |
| `recipient_name` | `str` | Optional | - |
| `recipient_phone` | `str` | Optional | - |
| `address` | [`GetAddressResponse`](../../doc/models/get-address-response.md) | Optional | - |
| `max_delivery_date` | `datetime` | Optional | Data máxima de entrega |
| `estimated_delivery_date` | `datetime` | Optional | Prazo estimado de entrega |
| `mtype` | `str` | Optional | Shipping Type |

## Example

```python
from pagarmeapisdk.models.get_shipping_response import GetShippingResponse

get_shipping_response = GetShippingResponse(
    amount=14,
    description='description6',
    recipient_name='recipient_name4',
    recipient_phone='recipient_phone8',
    address=None
)
```

