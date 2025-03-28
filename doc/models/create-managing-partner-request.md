
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

## Example (as JSON)

```json
{
  "name": "name4",
  "email": "email2",
  "document": "document2",
  "birthdate": "birthdate8",
  "monthly_income": 70,
  "professional_occupation": "professional_occupation8",
  "self_declared_legal_representative": false,
  "address": {
    "street": "street6",
    "complementary": "complementary8",
    "street_number": "street_number6",
    "neighborhood": "neighborhood2",
    "city": "city6",
    "state": "state2",
    "zip_code": "zip_code0",
    "reference_point": "reference_point0"
  },
  "phone_numbers": [
    {
      "ddd": "ddd4",
      "number": "number2",
      "type": "type0"
    }
  ],
  "mother_name": "mother_name0"
}
```

