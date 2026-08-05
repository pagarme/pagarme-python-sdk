
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
| `payment_origin` | [`GetPaymentOriginResponse`](../../doc/models/get-payment-origin-response.md) | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_charge_response import GetChargeResponse

get_charge_response = GetChargeResponse(
    id='id4',
    code='code2',
    gateway_id='gateway_id6',
    amount=116,
    status='status4',
    recurrency_cycle='"first" or "subsequent"'
)
```

