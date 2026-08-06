
# Get Increment Response

Response object for getting a increment

## Structure

`GetIncrementResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `value` | `float` | Optional | - |
| `increment_type` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `cycles` | `int` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |
| `description` | `str` | Optional | - |
| `subscription` | [`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md) | Optional | - |
| `subscription_item` | [`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md) | Optional | The Subscription Item |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_increment_response import GetIncrementResponse

get_increment_response = GetIncrementResponse(
    id='id2',
    value=68.64,
    increment_type='increment_type4',
    status='status6',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

