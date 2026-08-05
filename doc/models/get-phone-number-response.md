
# Get Phone Number Response

Response object for getting an PhoneNumberResponse

## Structure

`GetPhoneNumberResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ddd` | `str` | Optional | - |
| `number` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_phone_number_response import GetPhoneNumberResponse

get_phone_number_response = GetPhoneNumberResponse(
    ddd='ddd8',
    number='number4',
    mtype='type4'
)
```

