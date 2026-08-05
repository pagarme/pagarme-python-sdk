
# Create Google Pay Header Request

The GooglePay header request

## Structure

`CreateGooglePayHeaderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ephemeral_public_key` | `str` | Required | X.509 encoded key bytes, Base64 encoded as a string |

## Example

```python
from pagarmeapisdk.models.create_google_pay_header_request import CreateGooglePayHeaderRequest

create_google_pay_header_request = CreateGooglePayHeaderRequest(
    ephemeral_public_key='ephemeral_public_key0'
)
```

