
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
  "success_url": "success_url2",
  "payment_url": "payment_url6",
  "accepted_payment_methods": [
    "accepted_payment_methods3",
    "accepted_payment_methods4",
    "accepted_payment_methods5"
  ],
  "status": "status8",
  "customer": {
    "id": "id0",
    "name": "name0",
    "email": "email6",
    "delinquent": false,
    "created_at": "2016-03-13T12:52:32.123Z"
  }
}
```

