
# Get Plan Item Response

Response object for getting a plan item

## Structure

`GetPlanItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `pricing_scheme` | [`GetPricingSchemeResponse`](../../doc/models/get-pricing-scheme-response.md) | Optional | - |
| `description` | `str` | Optional | - |
| `plan` | [`GetPlanResponse`](../../doc/models/get-plan-response.md) | Optional | - |
| `quantity` | `int` | Optional | - |
| `cycles` | `int` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_plan_item_response import GetPlanItemResponse

get_plan_item_response = GetPlanItemResponse(
    id='id0',
    name='name0',
    status='status2',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

