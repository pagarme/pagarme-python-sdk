
# Get Register Information Response

Response object for getting an RegisterInformationResponse

## Structure

`GetRegisterInformationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | - |
| `document` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `site_url` | `str` | Optional | - |
| `phone_numbers` | [`List[GetPhoneNumberResponse]`](../../doc/models/get-phone-number-response.md) | Optional | - |
| `name` | `str` | Optional | - |
| `mother_name` | `str` | Optional | - |
| `birthdate` | `str` | Optional | - |
| `monthly_income` | `str` | Optional | - |
| `professional_occupation` | `str` | Optional | - |
| `address` | [`GetRegisterInformationAddressResponse`](../../doc/models/get-register-information-address-response.md) | Optional | - |
| `company_name` | `str` | Optional | - |
| `trading_name` | `str` | Optional | - |
| `annual_revenue` | `str` | Optional | - |
| `corporation_type` | `str` | Optional | - |
| `founding_date` | `str` | Optional | - |
| `cnae` | `str` | Optional | - |
| `main_address` | [`GetRegisterInformationAddressResponse`](../../doc/models/get-register-information-address-response.md) | Optional | - |
| `managing_partners` | [`List[GetManagingPartnerResponse]`](../../doc/models/get-managing-partner-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "email": "email2",
  "document": "document2",
  "type": "type6",
  "site_url": "site_url6",
  "phone_numbers": [
    {
      "ddd": "ddd4",
      "number": "number2",
      "type": "type0"
    },
    {
      "ddd": "ddd4",
      "number": "number2",
      "type": "type0"
    }
  ]
}
```

