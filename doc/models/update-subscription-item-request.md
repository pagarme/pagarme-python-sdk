
# Update Subscription Item Request

Request for updating a subscription item

## Structure

`UpdateSubscriptionItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `string` | Required | Description |
| `status` | `string` | Required | Status |
| `pricing_scheme` | [`UpdatePricingSchemeRequest`](../../doc/models/update-pricing-scheme-request.md) | Required | Pricing scheme |
| `name` | `string` | Required | Item name |
| `cycles` | `int` | Optional | Number of cycles that the item will be charged |
| `quantity` | `int` | Optional | Quantity |
| `minimum_price` | `int` | Optional | Minimum price |

## Example (as JSON)

```json
{
  "description": "description0",
  "status": "status8",
  "pricing_scheme": {
    "scheme_type": "scheme_type8",
    "price_brackets": [
      {
        "start_quantity": 119,
        "price": 57,
        "end_quantity": null,
        "overage_price": null
      },
      {
        "start_quantity": 120,
        "price": 58,
        "end_quantity": null,
        "overage_price": null
      },
      {
        "start_quantity": 121,
        "price": 59,
        "end_quantity": null,
        "overage_price": null
      }
    ],
    "price": null,
    "minimum_price": null,
    "percentage": null
  },
  "name": "name0",
  "cycles": null,
  "quantity": null,
  "minimum_price": null
}
```

