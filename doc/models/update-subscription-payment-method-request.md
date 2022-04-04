
# Update Subscription Payment Method Request

Request for updating a subscription's payment method

## Structure

`UpdateSubscriptionPaymentMethodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_method` | `string` | Required | The new payment method |
| `card_id` | `string` | Required | Card id |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Required | Card data |
| `card_token` | `string` | Optional | The Card Token |

## Example (as JSON)

```json
{
  "payment_method": null,
  "card_id": null,
  "card": {
    "number": null,
    "holder_name": null,
    "exp_month": null,
    "exp_year": null,
    "cvv": null,
    "billing_address": null,
    "brand": null,
    "billing_address_id": null,
    "metadata": null,
    "type": "credit",
    "options": null,
    "private_label": null,
    "label": null
  }
}
```

