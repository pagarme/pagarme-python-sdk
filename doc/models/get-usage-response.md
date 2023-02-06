
# Get Usage Response

Response object for getting a usage

## Structure

`GetUsageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Id |
| `quantity` | `int` | Optional | Quantity |
| `description` | `string` | Optional | Description |
| `used_at` | `datetime` | Optional | Used at |
| `created_at` | `datetime` | Optional | Creation date |
| `status` | `string` | Optional | Status |
| `deleted_at` | `datetime` | Optional | - |
| `subscription_item` | [`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md) | Optional | Subscription item |
| `code` | `string` | Optional | Identification code in the client system |
| `group` | `string` | Optional | Identification group in the client system |
| `amount` | `int` | Optional | Field used in item scheme type 'Percent' |

## Example (as JSON)

```json
{
  "id": null,
  "quantity": null,
  "description": null,
  "used_at": null,
  "created_at": null,
  "status": null,
  "deleted_at": null,
  "subscription_item": null,
  "code": null,
  "group": null,
  "amount": null
}
```

