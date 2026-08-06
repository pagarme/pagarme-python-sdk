
# Create Apple Pay Header Request

The ApplePay header request

## Structure

`CreateApplePayHeaderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_key_hash` | `str` | Optional | SHA–256 hash, Base64 string codified |
| `ephemeral_public_key` | `str` | Required | X.509 encoded key bytes, Base64 encoded as a string |
| `transaction_id` | `str` | Optional | Transaction identifier, generated on Device |

## Example

```python
from pagarmeapisdk.models.create_apple_pay_header_request import CreateApplePayHeaderRequest

create_apple_pay_header_request = CreateApplePayHeaderRequest(
    ephemeral_public_key='ephemeral_public_key4',
    public_key_hash='public_key_hash2',
    transaction_id='transaction_id2'
)
```

