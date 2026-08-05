
# Create Plan Item Request

Request for creating a plan item

## Structure

`CreatePlanItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Item name |
| `pricing_scheme` | [`CreatePricingSchemeRequest`](../../doc/models/create-pricing-scheme-request.md) | Required | Item's pricing scheme |
| `id` | `str` | Required | Item's id |
| `description` | `str` | Required | Item's description |
| `cycles` | `int` | Optional | Number of cycles where the item will be charged |
| `quantity` | `int` | Optional | Quantity |

## Example

```python
from pagarmeapisdk.models.create_plan_item_request import CreatePlanItemRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest

create_plan_item_request = CreatePlanItemRequest(
    name='name6',
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type=None
    ),
    id='id6',
    description='description6',
    cycles=6,
    quantity=230
)
```

