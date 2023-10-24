
# Get Plan Response

Response object for getting a plan

## Structure

`GetPlanResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `url` | `str` | Optional | - |
| `statement_descriptor` | `str` | Optional | - |
| `interval` | `str` | Optional | - |
| `interval_count` | `int` | Optional | - |
| `billing_type` | `str` | Optional | - |
| `payment_methods` | `List[str]` | Optional | - |
| `installments` | `List[int]` | Optional | - |
| `status` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `items` | [`List[GetPlanItemResponse]`](../../doc/models/get-plan-item-response.md) | Optional | - |
| `billing_days` | `List[int]` | Optional | - |
| `shippable` | `bool` | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `trial_period_days` | `int` | Optional | - |
| `minimum_price` | `int` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "description": "description0",
  "url": "url4",
  "statement_descriptor": "statement_descriptor0"
}
```

