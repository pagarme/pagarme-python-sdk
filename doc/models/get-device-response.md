
# Get Device Response

Response object for geetting an order device

## Structure

`GetDeviceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `platform` | `str` | Optional | Device's platform name |

## Example

```python
from pagarmeapisdk.models.get_device_response import GetDeviceResponse

get_device_response = GetDeviceResponse(
    platform='platform0'
)
```

