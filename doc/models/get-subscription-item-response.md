
# Get Subscription Item Response

## Structure

`GetSubscriptionItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `pricing_scheme` | [`GetPricingSchemeResponse`](../../doc/models/get-pricing-scheme-response.md) | Optional | - |
| `discounts` | [`List[GetDiscountResponse]`](../../doc/models/get-discount-response.md) | Optional | - |
| `increments` | [`List[GetIncrementResponse]`](../../doc/models/get-increment-response.md) | Optional | - |
| `subscription` | [`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md) | Optional | - |
| `name` | `str` | Optional | Item name |
| `quantity` | `int` | Optional | - |
| `cycles` | `int` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_subscription_item_response import GetSubscriptionItemResponse

get_subscription_item_response = GetSubscriptionItemResponse(
    id='id4',
    description='description4',
    status='status6',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

