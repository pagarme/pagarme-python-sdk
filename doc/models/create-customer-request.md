
# Create Customer Request

Request for creating a new customer

## Structure

`CreateCustomerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Name |
| `email` | `str` | Required | Email |
| `document` | `str` | Required | Document number. Only numbers, no special characters. |
| `mtype` | `str` | Required | Person type. Can be either 'individual' or 'company' |
| `address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | The customer's address |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `phones` | [`CreatePhonesRequest`](../../doc/models/create-phones-request.md) | Required | - |
| `code` | `str` | Required | Customer code |
| `gender` | `str` | Optional | Customer Gender |
| `document_type` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_customer_request import CreateCustomerRequest
from pagarmeapisdk.models.create_phones_request import CreatePhonesRequest

create_customer_request = CreateCustomerRequest(
    name='Tony Stark',
    email=None,
    document=None,
    mtype=None,
    address=CreateAddressRequest(
        street=None,
        number=None,
        zip_code=None,
        neighborhood=None,
        city=None,
        state=None,
        country=None,
        complement=None,
        line_1=None,
        line_2=None
    ),
    metadata={},
    phones=CreatePhonesRequest(),
    code=None,
    gender='gender6',
    document_type='document_type8'
)
```

