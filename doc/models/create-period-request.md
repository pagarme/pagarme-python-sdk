
# Create Period Request

## Structure

`CreatePeriodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_at` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_period_request import CreatePeriodRequest

create_period_request = CreatePeriodRequest(
    end_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

