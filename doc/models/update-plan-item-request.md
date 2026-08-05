
# Update Plan Item Request

Request for updating a plan item

## Structure

`UpdatePlanItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Item name |
| `description` | `str` | Required | Description |
| `status` | `str` | Required | Item status |
| `pricing_scheme` | [`UpdatePricingSchemeRequest`](../../doc/models/update-pricing-scheme-request.md) | Required | Pricing scheme |
| `quantity` | `int` | Optional | Quantity |
| `cycles` | `int` | Optional | Number of cycles that the item will be charged |

## Example

```python
from pagarmeapisdk.models.update_plan_item_request import UpdatePlanItemRequest
from pagarmeapisdk.models.update_pricing_scheme_request import UpdatePricingSchemeRequest

update_plan_item_request = UpdatePlanItemRequest(
    name=None,
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
    quantity=100,
    cycles=136
)
```

