
# Create Checkout Credit Card Payment Request

Checkout card payment request

## Structure

`CreateCheckoutCreditCardPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `string` | Optional | Card invoice text descriptor |
| `installments` | [`List of CreateCheckoutCardInstallmentOptionRequest`](../../doc/models/create-checkout-card-installment-option-request.md) | Optional | Payment installment options |
| `authentication` | [`CreatePaymentAuthenticationRequest`](../../doc/models/create-payment-authentication-request.md) | Optional | Creates payment authentication |
| `capture` | `bool` | Optional | Authorize and capture? |

## Example (as JSON)

```json
{
  "statement_descriptor": "statement_descriptor0",
  "installments": [
    {
      "number": 217,
      "total": 109
    },
    {
      "number": 218,
      "total": 110
    },
    {
      "number": 219,
      "total": 111
    }
  ],
  "authentication": {
    "type": "type2",
    "threed_secure": {
      "mpi": "mpi6",
      "cavv": "cavv2",
      "eci": "eci6",
      "transaction_id": "transaction_id4",
      "success_url": "success_url8",
      "ds_transaction_id": "ds_transaction_id4"
    }
  },
  "capture": false
}
```

