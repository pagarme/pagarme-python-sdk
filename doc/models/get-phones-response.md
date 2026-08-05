
# Get Phones Response

## Structure

`GetPhonesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `home_phone` | [`GetPhoneResponse`](../../doc/models/get-phone-response.md) | Optional | - |
| `mobile_phone` | [`GetPhoneResponse`](../../doc/models/get-phone-response.md) | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_phones_response import GetPhonesResponse

get_phones_response = GetPhonesResponse(
    home_phone=None,
    mobile_phone=None
)
```

