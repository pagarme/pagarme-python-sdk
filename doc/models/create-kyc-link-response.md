
# Create KYC Link Response

KYC Link

## Structure

`CreateKYCLinkResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `base_64` | `str` | Optional | Base64 |
| `url` | `str` | Optional | URL |
| `expiration_date` | `str` | Optional | Expiration Date |

## Example

```python
from pagarmeapisdk.models.create_kyc_link_response import CreateKYCLinkResponse

create_kyc_link_response = CreateKYCLinkResponse(
    base_64='base642',
    url='url4',
    expiration_date='expiration_date6'
)
```

