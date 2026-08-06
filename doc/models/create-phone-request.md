
# Create Phone Request

## Structure

`CreatePhoneRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | `str` | Optional | - |
| `number` | `str` | Optional | - |
| `area_code` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_phone_request import CreatePhoneRequest

create_phone_request = CreatePhoneRequest(
    country_code='country_code4',
    number='number2',
    area_code='area_code4',
    mtype='Type4'
)
```

