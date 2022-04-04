
# Create Subscription Item Request

Request for creating a new subscription item

## Structure

`CreateSubscriptionItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `string` | Required | Item description |
| `pricing_scheme` | [`CreatePricingSchemeRequest`](../../doc/models/create-pricing-scheme-request.md) | Required | Pricing scheme |
| `id` | `string` | Required | Item id |
| `plan_item_id` | `string` | Required | Plan item id |
| `discounts` | [`List of CreateDiscountRequest`](../../doc/models/create-discount-request.md) | Required | Discounts for the item |
| `name` | `string` | Required | Item name |
| `cycles` | `int` | Optional | Number of cycles which the item will be charged |
| `quantity` | `int` | Optional | Quantity of items |
| `minimum_price` | `int` | Optional | Minimum price |

## Example (as JSON)

```json
{
  "description": "description0",
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
  "id": "id0",
  "plan_item_id": "plan_item_id0",
  "discounts": [
    {
      "value": 10.23,
      "discount_type": "discount_type9",
      "item_id": "item_id1",
      "cycles": null,
      "description": null
    },
    {
      "value": 10.24,
      "discount_type": "discount_type0",
      "item_id": "item_id2",
      "cycles": null,
      "description": null
    },
    {
      "value": 10.25,
      "discount_type": "discount_type1",
      "item_id": "item_id3",
      "cycles": null,
      "description": null
    }
  ],
  "name": "name0",
  "cycles": null,
  "quantity": null,
  "minimum_price": null
}
```

