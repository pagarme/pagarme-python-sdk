
# Create Register Information Base Request

Request object for RegisterInformation.

## Structure

`CreateRegisterInformationBaseRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Required | - |
| `document` | `str` | Required | - |
| `mtype` | `str` | Required | "individual" ou "corporation" |
| `site_url` | `str` | Optional | - |
| `phone_numbers` | [`List[CreateRegisterInformationPhoneRequest]`](../../doc/models/create-register-information-phone-request.md) | Required | - |

## Example

```python
from pagarmeapisdk.models.create_register_information_base_request import CreateRegisterInformationBaseRequest

create_register_information_base_request = CreateRegisterInformationBaseRequest(
    email=None,
    document=None,
    mtype=None,
    phone_numbers=[
        None
    ],
    site_url='site_url2'
)
```

