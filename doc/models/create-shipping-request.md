
# Create Shipping Request

Shipping data

## Structure

`CreateShippingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Shipping amount |
| `description` | `str` | Required | Description |
| `recipient_name` | `str` | Required | Recipient name |
| `recipient_phone` | `str` | Required | Recipient phone number |
| `address_id` | `str` | Required | The id of the address that will be used for shipping |
| `address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | Address data |
| `max_delivery_date` | `datetime` | Optional | Data máxima de entrega |
| `estimated_delivery_date` | `datetime` | Optional | Prazo estimado de entrega |
| `mtype` | `str` | Required | Shipping type |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_shipping_request import CreateShippingRequest

create_shipping_request = CreateShippingRequest(
    amount=132,
    description='description8',
    recipient_name='recipient_name6',
    recipient_phone='recipient_phone0',
    address_id='address_id2',
    address=CreateAddressRequest(
        street=None,
        number=None,
        zip_code=None,
        neighborhood=None,
        city=None,
        state=None,
        country=None,
        complement=None,
        line_1=None,
        line_2=None
    ),
    mtype='type2',
    max_delivery_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    estimated_delivery_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

