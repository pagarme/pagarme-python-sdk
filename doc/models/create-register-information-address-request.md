
# Create Register Information Address Request

Register Information Address

## Structure

`CreateRegisterInformationAddressRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Required | - |
| `complementary` | `str` | Required | - |
| `street_number` | `str` | Required | - |
| `neighborhood` | `str` | Required | - |
| `city` | `str` | Required | - |
| `state` | `str` | Required | - |
| `zip_code` | `str` | Required | - |
| `reference_point` | `str` | Required | - |

## Example

```python
from pagarmeapisdk.models.create_register_information_address_request import CreateRegisterInformationAddressRequest

create_register_information_address_request = CreateRegisterInformationAddressRequest(
    street='street6',
    complementary='complementary8',
    street_number='street_number6',
    neighborhood='neighborhood2',
    city='city6',
    state='state2',
    zip_code='zip_code0',
    reference_point='reference_point0'
)
```

