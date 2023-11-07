
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

## Example (as JSON)

```json
{
  "name": "name0",
  "description": "description0",
  "statement_descriptor": "statement_descriptor0",
  "items": [
    {
      "name": "name8",
      "pricing_scheme": {
        "scheme_type": "scheme_type8",
        "price_brackets": [
          {
            "start_quantity": 144,
            "price": 174,
            "end_quantity": 152,
            "overage_price": 166
          },
          {
            "start_quantity": 144,
            "price": 174,
            "end_quantity": 152,
            "overage_price": 166
          },
          {
            "start_quantity": 144,
            "price": 174,
            "end_quantity": 152,
            "overage_price": 166
          }
        ],
        "price": 166,
        "minimum_price": 6,
        "percentage": 251.76
      },
      "id": "id8",
      "description": "description2",
      "cycles": 214,
      "quantity": 22
    }
  ],
  "shippable": false,
  "payment_methods": [
    "payment_methods5",
    "payment_methods4"
  ],
  "installments": [
    195,
    196
  ],
  "currency": "currency0",
  "interval": "interval8",
  "interval_count": 158,
  "billing_days": [
    159
  ],
  "billing_type": "billing_type4",
  "pricing_scheme": {
    "scheme_type": "scheme_type8",
    "price_brackets": [
      {
        "start_quantity": 144,
        "price": 174,
        "end_quantity": 152,
        "overage_price": 166
      },
      {
        "start_quantity": 144,
        "price": 174,
        "end_quantity": 152,
        "overage_price": 166
      },
      {
        "start_quantity": 144,
        "price": 174,
        "end_quantity": 152,
        "overage_price": 166
      }
    ],
    "price": 166,
    "minimum_price": 6,
    "percentage": 251.76
  },
  "metadata": {
    "key0": "metadata7"
  },
  "minimum_price": 156,
  "cycles": 164,
  "quantity": 144,
  "trial_period_days": 130
}
```

