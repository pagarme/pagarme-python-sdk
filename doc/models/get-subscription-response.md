
# Get Subscription Response

## Structure

`GetSubscriptionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `code` | `string` | Optional | - |
| `start_at` | `datetime` | Optional | - |
| `interval` | `string` | Optional | - |
| `interval_count` | `int` | Optional | - |
| `billing_type` | `string` | Optional | - |
| `current_cycle` | [`GetPeriodResponse`](../../doc/models/get-period-response.md) | Optional | - |
| `payment_method` | `string` | Optional | - |
| `currency` | `string` | Optional | - |
| `installments` | `int` | Optional | - |
| `status` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | - |
| `items` | [`List of GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md) | Optional | - |
| `statement_descriptor` | `string` | Optional | - |
| `metadata` | `dict` | Optional | - |
| `setup` | [`GetSetupResponse`](../../doc/models/get-setup-response.md) | Optional | - |
| `gateway_affiliation_id` | `string` | Optional | Affiliation Code |
| `next_billing_at` | `datetime` | Optional | - |
| `billing_day` | `int` | Optional | - |
| `minimum_price` | `int` | Optional | - |
| `canceled_at` | `datetime` | Optional | - |
| `discounts` | [`List of GetDiscountResponse`](../../doc/models/get-discount-response.md) | Optional | Subscription discounts |
| `increments` | [`List of GetIncrementResponse`](../../doc/models/get-increment-response.md) | Optional | Subscription increments |
| `boleto_due_days` | `int` | Optional | Days until boleto expires |
| `split` | [`GetSubscriptionSplitResponse`](../../doc/models/get-subscription-split-response.md) | Optional | Subscription's split response |
| `boleto` | [`GetSubscriptionBoletoResponse`](../../doc/models/get-subscription-boleto-response.md) | Optional | - |
| `manual_billing` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "boleto": {
    "interest": {
      "days": 2,
      "type": "percentage",
      "amount": 20
    },
    "fine": {
      "days": 2,
      "type": "flat",
      "amount": 10
    },
    "max_days_to_pay_past_due": 2
  }
}
```

