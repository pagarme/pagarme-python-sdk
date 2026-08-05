
# Get Location Response

Response object for geetting an order location request

## Structure

`GetLocationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `str` | Optional | Latitude |
| `longitude` | `str` | Optional | Longitude |

## Example

```python
from pagarmeapisdk.models.get_location_response import GetLocationResponse

get_location_response = GetLocationResponse(
    latitude='latitude6',
    longitude='longitude4'
)
```

