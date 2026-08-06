
# Create Register Information Corporation Request

## Structure

`CreateRegisterInformationCorporationRequest`

## Inherits From

[`CreateRegisterInformationBaseRequest`](../../doc/models/create-register-information-base-request.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_name` | `str` | Required | - |
| `trading_name` | `str` | Required | - |
| `annual_revenue` | `int` | Required | - |
| `corporation_type` | `str` | Optional | - |
| `founding_date` | `str` | Optional | - |
| `cnae` | `str` | Optional | - |
| `managing_partners` | [`List[CreateManagingPartnerRequest]`](../../doc/models/create-managing-partner-request.md) | Required | - |
| `main_address` | [`CreateRegisterInformationAddressRequest`](../../doc/models/create-register-information-address-request.md) | Required | - |

## Example

```python
from pagarmeapisdk.models.create_managing_partner_request import CreateManagingPartnerRequest
from pagarmeapisdk.models.create_register_information_address_request import CreateRegisterInformationAddressRequest
from pagarmeapisdk.models.create_register_information_base_request import CreateRegisterInformationCorporationRequest

create_register_information_corporation_request = CreateRegisterInformationCorporationRequest(
    email=None,
    document=None,
    mtype=None,
    phone_numbers=[
        None
    ],
    company_name=None,
    trading_name=None,
    annual_revenue=None,
    managing_partners=[
        CreateManagingPartnerRequest(
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
            mother_name='mother_name0'
        )
    ],
    main_address=CreateRegisterInformationAddressRequest(
        street=None,
        complementary=None,
        street_number=None,
        neighborhood=None,
        city=None,
        state=None,
        zip_code=None,
        reference_point=None
    ),
    corporation_type='corporation_type4',
    founding_date='founding_date4',
    cnae='cnae4',
    site_url='site_url4'
)
```

