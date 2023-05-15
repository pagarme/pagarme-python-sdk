
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
  "id": "id0",
  "quantity": 68,
  "description": "description0",
  "used_at": "2016-03-13T12:52:32.123Z",
  "created_at": "2016-03-13T12:52:32.123Z"
}
```

