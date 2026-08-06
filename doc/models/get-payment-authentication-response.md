
# Get Payment Authentication Response

Payment Authentication response

## Structure

`GetPaymentAuthenticationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `threed_secure` | [`GetThreeDSecureResponse`](../../doc/models/get-three-d-secure-response.md) | Optional | 3D-S payment authentication response |

## Example

```python
from pagarmeapisdk.models.get_payment_authentication_response import GetPaymentAuthenticationResponse

get_payment_authentication_response = GetPaymentAuthenticationResponse(
    mtype='type8',
    threed_secure=None
)
```

