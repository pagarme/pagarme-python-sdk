
# Create Three D Secure Request

Creates a 3D-S authentication payment

## Structure

`CreateThreeDSecureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mpi` | `str` | Required | The MPI Vendor (MerchantPlugin) |
| `cavv` | `str` | Optional | The Cardholder Authentication Verification value |
| `eci` | `str` | Optional | The Electronic Commerce Indicator value |
| `transaction_id` | `str` | Optional | The TransactionId value (XID) |
| `success_url` | `str` | Optional | The success URL after the authentication |
| `ds_transaction_id` | `str` | Optional | Directory Service Transaction Identifier |
| `version` | `str` | Optional | ThreeDSecure Version |

## Example

```python
from pagarmeapisdk.models.create_three_d_secure_request import CreateThreeDSecureRequest

create_three_d_secure_request = CreateThreeDSecureRequest(
    mpi='mpi2',
    cavv='cavv6',
    eci='eci0',
    transaction_id='transaction_id8',
    success_url='success_url2',
    ds_transaction_id='ds_transaction_id8'
)
```

