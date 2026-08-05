
# Create Location Request

Request for creating a location

## Structure

`CreateLocationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `str` | Required | Latitude |
| `longitude` | `str` | Required | Longitude |

## Example

```python
from pagarmeapisdk.models.create_location_request import CreateLocationRequest

create_location_request = CreateLocationRequest(
    latitude='latitude2',
    longitude='longitude2'
)
```

