
# Create Register Information Individual Request

## Structure

`CreateRegisterInformationIndividualRequest`

## Inherits From

[`CreateRegisterInformationBaseRequest`](../../doc/models/create-register-information-base-request.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `mother_name` | `str` | Optional | - |
| `birthdate` | `str` | Required | - |
| `monthly_income` | `int` | Required | - |
| `professional_occupation` | `str` | Required | - |
| `address` | [`CreateRegisterInformationAddressRequest`](../../doc/models/create-register-information-address-request.md) | Required | - |

## Example

```python
from pagarmeapisdk.models.create_register_information_address_request import CreateRegisterInformationAddressRequest
from pagarmeapisdk.models.create_register_information_base_request import CreateRegisterInformationIndividualRequest
from pagarmeapisdk.models.create_register_information_phone_request import CreateRegisterInformationPhoneRequest

create_register_information_individual_request = CreateRegisterInformationIndividualRequest(
    email='email4',
    document='document6',
    mtype='type8',
    phone_numbers=[
        None,
        CreateRegisterInformationPhoneRequest(
            ddd=None,
            number=None,
            mtype=None
        )
    ],
    name='name6',
    birthdate='birthdate0',
    monthly_income=196,
    professional_occupation='professional_occupation0',
    address=CreateRegisterInformationAddressRequest(
        street=None,
        complementary=None,
        street_number=None,
        neighborhood=None,
        city=None,
        state=None,
        zip_code=None,
        reference_point=None
    ),
    mother_name='mother_name2',
    site_url='site_url4'
)
```

