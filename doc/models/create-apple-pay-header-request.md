
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

## Example (as JSON)

```json
{
  "public_key_hash": "public_key_hash8",
  "ephemeral_public_key": "ephemeral_public_key0",
  "transaction_id": "transaction_id8"
}
```

