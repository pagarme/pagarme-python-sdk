
# Update Plan Request

Request for updating a plan

## Structure

`UpdatePlanRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | Plan's name |
| `description` | `string` | Required | Description |
| `installments` | `List of int` | Required | Number os installments |
| `statement_descriptor` | `string` | Required | Text that will be shown on the credit card's statement |
| `currency` | `string` | Required | Currency |
| `interval` | `string` | Required | Interval |
| `interval_count` | `int` | Required | Interval count |
| `payment_methods` | `List of string` | Required | Payment methods accepted by the plan |
| `billing_type` | `string` | Required | Billing type |
| `status` | `string` | Required | Plan status |
| `shippable` | `bool` | Required | Indicates if the plan is shippable |
| `billing_days` | `List of int` | Required | Billing days accepted by the plan |
| `metadata` | `dict` | Required | Metadata |
| `minimum_price` | `int` | Optional | Minimum price |
| `trial_period_days` | `int` | Optional | Number of trial period in days, where the customer will not be charged |

## Example (as JSON)

```json
{
  "name": "name0",
  "description": "description0",
  "installments": [
    119,
    120,
    121
  ],
  "statement_descriptor": "statement_descriptor0",
  "currency": "currency0",
  "interval": "interval2",
  "interval_count": 82,
  "payment_methods": [
    "payment_methods5",
    "payment_methods6"
  ],
  "billing_type": "billing_type6",
  "status": "status8",
  "shippable": false,
  "billing_days": [
    143,
    144,
    145
  ],
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  },
  "minimum_price": null,
  "trial_period_days": null
}
```

