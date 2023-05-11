
# Get Subscription Item Response

## Structure

`GetSubscriptionItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `description` | `string` | Optional | - |
| `status` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `pricing_scheme` | [`GetPricingSchemeResponse`](../../doc/models/get-pricing-scheme-response.md) | Optional | - |
| `discounts` | [`List of GetDiscountResponse`](../../doc/models/get-discount-response.md) | Optional | - |
| `increments` | [`List of GetIncrementResponse`](../../doc/models/get-increment-response.md) | Optional | - |
| `subscription` | [`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md) | Optional | - |
| `name` | `string` | Optional | Item name |
| `quantity` | `int` | Optional | - |
| `cycles` | `int` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "description": "description0",
  "status": "status8",
  "created_at": "2016-03-13T12:52:32.123Z",
  "updated_at": "2016-03-13T12:52:32.123Z"
}
```

