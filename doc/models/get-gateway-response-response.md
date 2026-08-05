
# Get Gateway Response Response

The Transaction Gateway Response

## Structure

`GetGatewayResponseResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The error code |
| `errors` | [`List[GetGatewayErrorResponse]`](../../doc/models/get-gateway-error-response.md) | Optional | The gateway response errors list |

## Example

```python
from pagarmeapisdk.models.get_gateway_error_response import GetGatewayErrorResponse
from pagarmeapisdk.models.get_gateway_response_response import GetGatewayResponseResponse

get_gateway_response_response = GetGatewayResponseResponse(
    code='code0',
    errors=[
        None,
        GetGatewayErrorResponse()
    ]
)
```

