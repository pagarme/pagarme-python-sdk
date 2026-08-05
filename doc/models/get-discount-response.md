
# Get Discount Response

Response object for getting a discount

## Structure

`GetDiscountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `value` | `float` | Optional | - |
| `discount_type` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `cycles` | `int` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |
| `description` | `str` | Optional | - |
| `subscription` | [`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md) | Optional | - |
| `subscription_item` | [`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md) | Optional | The subscription item |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_discount_response import GetDiscountResponse

get_discount_response = GetDiscountResponse(
    id='id4',
    value=163.56,
    discount_type='discount_type2',
    status='status6',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

