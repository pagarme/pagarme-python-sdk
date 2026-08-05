
# Update Plan Request

Request for updating a plan

## Structure

`UpdatePlanRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Plan's name |
| `description` | `str` | Required | Description |
| `installments` | `List[int]` | Required | Number os installments |
| `statement_descriptor` | `str` | Required | Text that will be shown on the credit card's statement |
| `currency` | `str` | Required | Currency |
| `interval` | `str` | Required | Interval |
| `interval_count` | `int` | Required | Interval count |
| `payment_methods` | `List[str]` | Required | Payment methods accepted by the plan |
| `billing_type` | `str` | Required | Billing type |
| `status` | `str` | Required | Plan status |
| `shippable` | `bool` | Required | Indicates if the plan is shippable |
| `billing_days` | `List[int]` | Required | Billing days accepted by the plan |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `minimum_price` | `int` | Optional | Minimum price |
| `trial_period_days` | `int` | Optional | Number of trial period in days, where the customer will not be charged |

## Example

```python
from pagarmeapisdk.models.update_plan_request import UpdatePlanRequest

update_plan_request = UpdatePlanRequest(
    name='name0',
    description='description0',
    installments=[
        73,
        74
    ],
    statement_descriptor='statement_descriptor0',
    currency='currency0',
    interval='interval8',
    interval_count=36,
    payment_methods=[
        'payment_methods5',
        'payment_methods4',
        'payment_methods3'
    ],
    billing_type='billing_type6',
    status='status2',
    shippable=False,
    billing_days=[
        37
    ],
    metadata={
        'key0': 'metadata3'
    },
    minimum_price=222,
    trial_period_days=8
)
```

