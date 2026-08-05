
# Create Phones Request

## Structure

`CreatePhonesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `home_phone` | [`CreatePhoneRequest`](../../doc/models/create-phone-request.md) | Optional | - |
| `mobile_phone` | [`CreatePhoneRequest`](../../doc/models/create-phone-request.md) | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_phone_request import CreatePhoneRequest
from pagarmeapisdk.models.create_phones_request import CreatePhonesRequest

create_phones_request = CreatePhonesRequest(
    home_phone=CreatePhoneRequest(),
    mobile_phone=CreatePhoneRequest()
)
```

