
# Create Payment Authentication Request

The payment authentication request

## Structure

`CreatePaymentAuthenticationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | The Authentication type |
| `threed_secure` | [`CreateThreeDSecureRequest`](../../doc/models/create-three-d-secure-request.md) | Required | The 3D-S authentication object |

## Example

```python
from pagarmeapisdk.models.create_payment_authentication_request import CreatePaymentAuthenticationRequest
from pagarmeapisdk.models.create_three_d_secure_request import CreateThreeDSecureRequest

create_payment_authentication_request = CreatePaymentAuthenticationRequest(
    mtype='type2',
    threed_secure=CreateThreeDSecureRequest(
        mpi=None
    )
)
```

