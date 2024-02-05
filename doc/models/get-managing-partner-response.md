
# Get Managing Partner Response

Response object for getting an ManagingPartnerResponse

## Structure

`GetManagingPartnerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `document` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `mother_name` | `str` | Optional | - |
| `birthdate` | `str` | Optional | - |
| `monthly_income` | `str` | Optional | - |
| `professional_occupation` | `str` | Optional | - |
| `self_declared_representative` | `bool` | Optional | - |
| `address` | [`GetRegisterInformationAddressResponse`](../../doc/models/get-register-information-address-response.md) | Optional | - |
| `phone_numbers` | [`List[GetPhoneNumberResponse]`](../../doc/models/get-phone-number-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "name": "name0",
  "email": "email6",
  "document": "document6",
  "type": "type0",
  "mother_name": "mother_name6"
}
```

