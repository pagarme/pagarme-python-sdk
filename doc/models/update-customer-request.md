
# Update Customer Request

Request for updating a customer

## Structure

`UpdateCustomerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name |
| `email` | `str` | Optional | Email |
| `document` | `str` | Optional | Document number |
| `mtype` | `str` | Optional | Person type |
| `address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Optional | Address |
| `metadata` | `Dict[str, str]` | Optional | Metadata |
| `phones` | [`CreatePhonesRequest`](../../doc/models/create-phones-request.md) | Optional | - |
| `code` | `str` | Optional | Código de referência do cliente no sistema da loja. Max: 52 caracteres |
| `gender` | `str` | Optional | Gênero do cliente |
| `document_type` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.update_customer_request import UpdateCustomerRequest

update_customer_request = UpdateCustomerRequest(
    name='name8',
    email='email8',
    document='document2',
    mtype='type8',
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
    )
)
```

