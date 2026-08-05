
# Create Register Information Phone Request

Register Information Phone

## Structure

`CreateRegisterInformationPhoneRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ddd` | `str` | Required | - |
| `number` | `str` | Required | - |
| `mtype` | `str` | Required | - |

## Example

```python
from pagarmeapisdk.models.create_register_information_phone_request import CreateRegisterInformationPhoneRequest

create_register_information_phone_request = CreateRegisterInformationPhoneRequest(
    ddd='ddd4',
    number='number2',
    mtype='type0'
)
```

