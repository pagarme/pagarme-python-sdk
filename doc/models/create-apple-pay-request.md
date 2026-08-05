
# Create Apple Pay Request

The ApplePay Token Payment Request

## Structure

`CreateApplePayRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Required | The token version |
| `data` | `str` | Required | The cryptography data |
| `header` | [`CreateApplePayHeaderRequest`](../../doc/models/create-apple-pay-header-request.md) | Required | The ApplePay header request |
| `signature` | `str` | Required | Detached PKCS #7 signature, Base64 encoded as string |
| `merchant_identifier` | `str` | Required | ApplePay Merchant identifier |

## Example

```python
from pagarmeapisdk.models.create_apple_pay_header_request import CreateApplePayHeaderRequest
from pagarmeapisdk.models.create_apple_pay_request import CreateApplePayRequest

create_apple_pay_request = CreateApplePayRequest(
    version='version0',
    data='data4',
    header=CreateApplePayHeaderRequest(
        ephemeral_public_key=None
    ),
    signature='signature2',
    merchant_identifier='merchant_identifier8'
)
```

