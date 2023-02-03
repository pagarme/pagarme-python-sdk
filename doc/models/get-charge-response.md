
# Get Charge Response

Response object for getting a charge

## Structure

`GetChargeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `code` | `string` | Optional | - |
| `gateway_id` | `string` | Optional | - |
| `amount` | `int` | Optional | - |
| `status` | `string` | Optional | - |
| `currency` | `string` | Optional | - |
| `payment_method` | `string` | Optional | - |
| `due_at` | `datetime` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `last_transaction` | [`GetTransactionResponse`](../../doc/models/get-transaction-response.md) | Optional | - |
| `invoice` | [`GetInvoiceResponse`](../../doc/models/get-invoice-response.md) | Optional | - |
| `order` | [`GetOrderResponse`](../../doc/models/get-order-response.md) | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `metadata` | `dict` | Optional | - |
| `paid_at` | `datetime` | Optional | - |
| `canceled_at` | `datetime` | Optional | - |
| `canceled_amount` | `int` | Optional | Canceled Amount |
| `paid_amount` | `int` | Optional | Paid amount |
| `interest_and_fine_paid` | `int` | Optional | interest and fine paid |
| `recurrency_cycle` | `string` | Optional | Defines whether the card has been used one or more times. |

## Example (as JSON)

```json
{
  "id": null,
  "code": null,
  "gateway_id": null,
  "amount": null,
  "status": null,
  "currency": null,
  "payment_method": null,
  "due_at": null,
  "created_at": null,
  "updated_at": null,
  "last_transaction": null,
  "invoice": null,
  "order": null,
  "customer": null,
  "metadata": null,
  "paid_at": null,
  "canceled_at": null,
  "canceled_amount": null,
  "paid_amount": null,
  "interest_and_fine_paid": null,
  "recurrency_cycle": null
}
```

