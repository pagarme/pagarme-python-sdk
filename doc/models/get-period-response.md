
# Get Period Response

Response object for getting a period

## Structure

`GetPeriodResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_at` | `datetime` | Optional | - |
| `end_at` | `datetime` | Optional | - |
| `id` | `str` | Optional | - |
| `billing_at` | `datetime` | Optional | - |
| `subscription` | [`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md) | Optional | - |
| `status` | `str` | Optional | - |
| `duration` | `int` | Optional | - |
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `cycle` | `int` | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_period_response import GetPeriodResponse

get_period_response = GetPeriodResponse(
    start_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    end_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id8',
    billing_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    subscription=None
)
```

