
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

## Example (as JSON)

```json
{
  "name": "name0",
  "description": "description0",
  "installments": [
    121,
    122,
    123
  ],
  "statement_descriptor": "statement_descriptor0",
  "currency": "currency0",
  "interval": "interval8",
  "interval_count": 84,
  "payment_methods": [
    "payment_methods5",
    "payment_methods6"
  ],
  "billing_type": "billing_type6",
  "status": "status8",
  "shippable": false,
  "billing_days": [
    171,
    170
  ],
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  },
  "minimum_price": 174,
  "trial_period_days": 56
}
```

