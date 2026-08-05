
# Get Register Information Address Response

Response object for getting an RegisterInformationAddress

## Structure

`GetRegisterInformationAddressResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Optional | - |
| `complementary` | `str` | Optional | - |
| `street_number` | `str` | Optional | - |
| `neighborhood` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `zip_code` | `str` | Optional | - |
| `reference_point` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_register_information_address_response import GetRegisterInformationAddressResponse

get_register_information_address_response = GetRegisterInformationAddressResponse(
    street='street2',
    complementary='complementary4',
    street_number='street_number2',
    neighborhood='neighborhood8',
    city='city8'
)
```

