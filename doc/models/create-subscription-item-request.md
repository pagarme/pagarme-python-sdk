
# Create Subscription Item Request

Request for creating a new subscription item

## Structure

`CreateSubscriptionItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | Item description |
| `pricing_scheme` | [`CreatePricingSchemeRequest`](../../doc/models/create-pricing-scheme-request.md) | Required | Pricing scheme |
| `id` | `str` | Required | Item id |
| `plan_item_id` | `str` | Required | Plan item id |
| `discounts` | [`List[CreateDiscountRequest]`](../../doc/models/create-discount-request.md) | Required | Discounts for the item |
| `name` | `str` | Required | Item name |
| `cycles` | `int` | Optional | Number of cycles which the item will be charged |
| `quantity` | `int` | Optional | Quantity of items |
| `minimum_price` | `int` | Optional | Minimum price |

## Example

```python
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest
from pagarmeapisdk.models.create_subscription_item_request import CreateSubscriptionItemRequest

create_subscription_item_request = CreateSubscriptionItemRequest(
    description=None,
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type=None
    ),
    id=None,
    plan_item_id=None,
    discounts=[
        None
    ],
    name=None,
    cycles=44,
    quantity=24,
    minimum_price=36
)
```

