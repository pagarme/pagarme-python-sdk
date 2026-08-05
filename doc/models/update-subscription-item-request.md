
# Update Subscription Item Request

Request for updating a subscription item

## Structure

`UpdateSubscriptionItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | Description |
| `status` | `str` | Required | Status |
| `pricing_scheme` | [`UpdatePricingSchemeRequest`](../../doc/models/update-pricing-scheme-request.md) | Required | Pricing scheme |
| `name` | `str` | Required | Item name |
| `cycles` | `int` | Optional | Number of cycles that the item will be charged |
| `quantity` | `int` | Optional | Quantity |
| `minimum_price` | `int` | Optional | Minimum price |

## Example

```python
from pagarmeapisdk.models.update_pricing_scheme_request import UpdatePricingSchemeRequest
from pagarmeapisdk.models.update_subscription_item_request import UpdateSubscriptionItemRequest

update_subscription_item_request = UpdateSubscriptionItemRequest(
    description=None,
    status=None,
    pricing_scheme=UpdatePricingSchemeRequest(
        scheme_type=None,
        price_brackets=[
            None
        ],
        price=166,
        minimum_price=6,
        percentage=251.76
    ),
    name=None,
    cycles=14,
    quantity=222,
    minimum_price=22
)
```

