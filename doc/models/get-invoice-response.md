
# Get Invoice Response

Response object for getting an invoice

## Structure

`GetInvoiceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `url` | `str` | Optional | - |
| `amount` | `int` | Optional | - |
| `status` | `str` | Optional | - |
| `payment_method` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `items` | [`List[GetInvoiceItemResponse]`](../../doc/models/get-invoice-item-response.md) | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `charge` | [`GetChargeResponse`](../../doc/models/get-charge-response.md) | Optional | - |
| `installments` | `int` | Optional | - |
| `billing_address` | [`GetBillingAddressResponse`](../../doc/models/get-billing-address-response.md) | Optional | - |
| `subscription` | [`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md) | Optional | - |
| `cycle` | [`GetPeriodResponse`](../../doc/models/get-period-response.md) | Optional | - |
| `shipping` | [`GetShippingResponse`](../../doc/models/get-shipping-response.md) | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `due_at` | `datetime` | Optional | - |
| `canceled_at` | `datetime` | Optional | - |
| `billing_at` | `datetime` | Optional | - |
| `seen_at` | `datetime` | Optional | - |
| `total_discount` | `int` | Optional | Total discounted value |
| `total_increment` | `int` | Optional | Total discounted value |
| `subscription_id` | `str` | Optional | Subscription Id |

## Example (as JSON)

```json
{
  "id": "id0",
  "code": "code8",
  "url": "url4",
  "amount": 168,
  "status": "status8"
}
```

