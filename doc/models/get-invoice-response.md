
# Get Invoice Response

Response object for getting an invoice

## Structure

`GetInvoiceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `code` | `string` | Optional | - |
| `url` | `string` | Optional | - |
| `amount` | `int` | Optional | - |
| `status` | `string` | Optional | - |
| `payment_method` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `items` | [`List of GetInvoiceItemResponse`](../../doc/models/get-invoice-item-response.md) | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `charge` | [`GetChargeResponse`](../../doc/models/get-charge-response.md) | Optional | - |
| `installments` | `int` | Optional | - |
| `billing_address` | [`GetBillingAddressResponse`](../../doc/models/get-billing-address-response.md) | Optional | - |
| `subscription` | [`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md) | Optional | - |
| `cycle` | [`GetPeriodResponse`](../../doc/models/get-period-response.md) | Optional | - |
| `shipping` | [`GetShippingResponse`](../../doc/models/get-shipping-response.md) | Optional | - |
| `metadata` | `dict` | Optional | - |
| `due_at` | `datetime` | Optional | - |
| `canceled_at` | `datetime` | Optional | - |
| `billing_at` | `datetime` | Optional | - |
| `seen_at` | `datetime` | Optional | - |
| `total_discount` | `int` | Optional | Total discounted value |
| `total_increment` | `int` | Optional | Total discounted value |
| `subscription_id` | `string` | Optional | Subscription Id |

## Example (as JSON)

```json
{
  "id": null,
  "code": null,
  "url": null,
  "amount": null,
  "status": null,
  "payment_method": null,
  "created_at": null,
  "items": null,
  "customer": null,
  "charge": null,
  "installments": null,
  "billing_address": null,
  "subscription": null,
  "cycle": null,
  "shipping": null,
  "metadata": null,
  "due_at": null,
  "canceled_at": null,
  "billing_at": null,
  "seen_at": null,
  "total_discount": null,
  "total_increment": null,
  "subscription_id": null
}
```

