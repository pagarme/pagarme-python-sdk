
# Get Charge Response

Response object for getting a charge

## Structure

`GetChargeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `gateway_id` | `str` | Optional | - |
| `amount` | `int` | Optional | - |
| `status` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `payment_method` | `str` | Optional | - |
| `due_at` | `datetime` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `last_transaction` | [`GetTransactionResponse`](../../doc/models/get-transaction-response.md) | Optional | - |
| `invoice` | [`GetInvoiceResponse`](../../doc/models/get-invoice-response.md) | Optional | - |
| `order` | [`GetOrderResponse`](../../doc/models/get-order-response.md) | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `paid_at` | `datetime` | Optional | - |
| `canceled_at` | `datetime` | Optional | - |
| `canceled_amount` | `int` | Optional | Canceled Amount |
| `paid_amount` | `int` | Optional | Paid amount |
| `interest_and_fine_paid` | `int` | Optional | interest and fine paid |
| `recurrency_cycle` | `str` | Optional | Defines whether the card has been used one or more times. |

## Example (as JSON)

```json
{
  "recurrency_cycle": "\"first\" or \"subsequent\"",
  "id": "id0",
  "code": "code8",
  "gateway_id": "gateway_id0",
  "amount": 164,
  "status": "status2"
}
```

