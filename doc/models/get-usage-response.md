
# Get Usage Response

Response object for getting a usage

## Structure

`GetUsageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Id |
| `quantity` | `int` | Optional | Quantity |
| `description` | `str` | Optional | Description |
| `used_at` | `datetime` | Optional | Used at |
| `created_at` | `datetime` | Optional | Creation date |
| `status` | `str` | Optional | Status |
| `deleted_at` | `datetime` | Optional | - |
| `subscription_item` | [`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md) | Optional | Subscription item |
| `code` | `str` | Optional | Identification code in the client system |
| `group` | `str` | Optional | Identification group in the client system |
| `amount` | `int` | Optional | Field used in item scheme type 'Percent' |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_usage_response import GetUsageResponse

get_usage_response = GetUsageResponse(
    id='id4',
    quantity=246,
    description='description4',
    used_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

