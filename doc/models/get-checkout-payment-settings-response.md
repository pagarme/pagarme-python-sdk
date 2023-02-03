
# Get Checkout Payment Settings Response

Checkout Payment Settings Response

## Structure

`GetCheckoutPaymentSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success_url` | `string` | Optional | Success Url |
| `payment_url` | `string` | Optional | Payment Url |
| `accepted_payment_methods` | `List of string` | Optional | Accepted Payment Methods |
| `status` | `string` | Optional | Status |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | Customer |
| `amount` | `int` | Optional | Payment amount |
| `default_payment_method` | `string` | Optional | Default Payment Method |
| `gateway_affiliation_id` | `string` | Optional | Gateway Affiliation Id |

## Example (as JSON)

```json
{
  "success_url": null,
  "payment_url": null,
  "accepted_payment_methods": null,
  "status": null,
  "customer": null,
  "amount": null,
  "default_payment_method": null,
  "gateway_affiliation_id": null
}
```

