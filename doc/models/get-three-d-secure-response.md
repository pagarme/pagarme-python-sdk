
# Get Three D Secure Response

3D-S payment authentication response

## Structure

`GetThreeDSecureResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mpi` | `str` | Optional | MPI Vendor |
| `eci` | `str` | Optional | Electronic Commerce Indicator (ECI) (Opcional) |
| `cavv` | `str` | Optional | Online payment cryptogram, definido pelo 3-D Secure. |
| `transaction_id` | `str` | Optional | Identificador da transação (XID) |
| `success_url` | `str` | Optional | Url de redirecionamento de sucessso |

## Example

```python
from pagarmeapisdk.models.get_three_d_secure_response import GetThreeDSecureResponse

get_three_d_secure_response = GetThreeDSecureResponse(
    mpi='mpi2',
    eci='eci0',
    cavv='cavv6',
    transaction_id='transaction_Id4',
    success_url='success_url2'
)
```

