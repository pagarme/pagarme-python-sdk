
# Create Plan Request

Request for creating a plan

## Structure

`CreatePlanRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Plan's name |
| `description` | `str` | Required | Description |
| `statement_descriptor` | `str` | Required | Text that will be printed on the credit card's statement |
| `items` | [`List[CreatePlanItemRequest]`](../../doc/models/create-plan-item-request.md) | Required | Plan items |
| `shippable` | `bool` | Required | Indicates if the plan is shippable |
| `payment_methods` | `List[str]` | Required | Allowed payment methods for the plan |
| `installments` | `List[int]` | Required | Number of installments |
| `currency` | `str` | Required | Currency |
| `interval` | `str` | Required | Interval |
| `interval_count` | `int` | Required | Interval counts between two charges. For instance, if the interval is 'month' and count is 2, the customer will be charged once every two months. |
| `billing_days` | `List[int]` | Required | Allowed billings days for the subscription, in case the plan type is 'exact_day' |
| `billing_type` | `str` | Required | Billing type |
| `pricing_scheme` | [`CreatePricingSchemeRequest`](../../doc/models/create-pricing-scheme-request.md) | Required | Plan's pricing scheme |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `minimum_price` | `int` | Optional | Minimum price that will be charged |
| `cycles` | `int` | Optional | Number of cycles |
| `quantity` | `int` | Optional | Quantity |
| `trial_period_days` | `int` | Optional | Trial period, where the customer will not be charged. |

## Example

```python
from pagarmeapisdk.models.create_plan_request import CreatePlanRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest

create_plan_request = CreatePlanRequest(
    name=None,
    description=None,
    statement_descriptor=None,
    items=[
        None
    ],
    shippable=None,
    payment_methods=[],
    installments=[],
    currency=None,
    interval=None,
    interval_count=None,
    billing_days=[],
    billing_type=None,
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type=None
    ),
    metadata={},
    minimum_price=28,
    cycles=36,
    quantity=16,
    trial_period_days=2
)
```

