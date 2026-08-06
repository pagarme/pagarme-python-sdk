
# Create Managing Partner Request

Managing Partner Request

## Structure

`CreateManagingPartnerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `email` | `str` | Required | - |
| `document` | `str` | Required | - |
| `mother_name` | `str` | Optional | - |
| `birthdate` | `str` | Required | - |
| `monthly_income` | `int` | Required | - |
| `professional_occupation` | `str` | Required | - |
| `self_declared_legal_representative` | `bool` | Required | - |
| `address` | [`CreateRegisterInformationAddressRequest`](../../doc/models/create-register-information-address-request.md) | Required | - |
| `phone_numbers` | [`List[CreateRegisterInformationPhoneRequest]`](../../doc/models/create-register-information-phone-request.md) | Required | - |

## Example

```python
from pagarmeapisdk.models.create_managing_partner_request import CreateManagingPartnerRequest
from pagarmeapisdk.models.create_register_information_address_request import CreateRegisterInformationAddressRequest

create_managing_partner_request = CreateManagingPartnerRequest(
    name=None,
    email=None,
    document=None,
    birthdate=None,
    monthly_income=None,
    professional_occupation=None,
    self_declared_legal_representative=None,
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
    phone_numbers=[
        None
    ],
    mother_name='mother_name2'
)
```

