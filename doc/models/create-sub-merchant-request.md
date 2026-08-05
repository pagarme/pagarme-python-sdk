
# Create Sub Merchant Request

SubMerchant

## Structure

`CreateSubMerchantRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_facilitator_code` | `str` | Required | Payment Facilitator Code |
| `code` | `str` | Required | Code |
| `name` | `str` | Required | Name |
| `merchant_category_code` | `str` | Required | Merchant Category Code |
| `document` | `str` | Required | Document number. Only numbers, no special characters. |
| `mtype` | `str` | Required | Document type. Can be either 'individual' or 'company' |
| `phone` | [`CreatePhoneRequest`](../../doc/models/create-phone-request.md) | Required | Phone |
| `address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | Address |
| `legal_name` | `str` | Required | Legal name |
| `site_url` | `str` | Required | Site Url |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_phone_request import CreatePhoneRequest
from pagarmeapisdk.models.create_sub_merchant_request import CreateSubMerchantRequest

create_sub_merchant_request = CreateSubMerchantRequest(
    payment_facilitator_code='payment_facilitator_code8',
    code='code6',
    name='name8',
    merchant_category_code='merchant_category_code2',
    document='document8',
    mtype='type2',
    phone=CreatePhoneRequest(),
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
    legal_name='legal_name6',
    site_url='site_url0'
)
```

