
# Get Plan Response

Response object for getting a plan

## Structure

`GetPlanResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `description` | `string` | Optional | - |
| `url` | `string` | Optional | - |
| `statement_descriptor` | `string` | Optional | - |
| `interval` | `string` | Optional | - |
| `interval_count` | `int` | Optional | - |
| `billing_type` | `string` | Optional | - |
| `payment_methods` | `List of string` | Optional | - |
| `installments` | `List of int` | Optional | - |
| `status` | `string` | Optional | - |
| `currency` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `items` | [`List of GetPlanItemResponse`](../../doc/models/get-plan-item-response.md) | Optional | - |
| `billing_days` | `List of int` | Optional | - |
| `shippable` | `bool` | Optional | - |
| `metadata` | `dict` | Optional | - |
| `trial_period_days` | `int` | Optional | - |
| `minimum_price` | `int` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "description": null,
  "url": null,
  "statement_descriptor": null,
  "interval": null,
  "interval_count": null,
  "billing_type": null,
  "payment_methods": null,
  "installments": null,
  "status": null,
  "currency": null,
  "created_at": null,
  "updated_at": null,
  "items": null,
  "billing_days": null,
  "shippable": null,
  "metadata": null,
  "trial_period_days": null,
  "minimum_price": null,
  "deleted_at": null
}
```

