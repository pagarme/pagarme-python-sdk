
# Create Device Request

Request for creating a device

## Structure

`CreateDeviceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `platform` | `str` | Optional | Device's platform |

## Example

```python
from pagarmeapisdk.models.create_device_request import CreateDeviceRequest

create_device_request = CreateDeviceRequest(
    platform='platform0'
)
```

