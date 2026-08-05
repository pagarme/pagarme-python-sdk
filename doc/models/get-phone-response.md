
# Get Phone Response

## Structure

`GetPhoneResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | `str` | Optional | - |
| `number` | `str` | Optional | - |
| `area_code` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_phone_response import GetPhoneResponse

get_phone_response = GetPhoneResponse(
    country_code='country_code0',
    number='number8',
    area_code='area_code0'
)
```

