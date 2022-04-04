
# Get Checkout Credit Card Payment Response

## Structure

`GetCheckoutCreditCardPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `string` | Required | Descrição na fatura |
| `installments` | [`List of GetCheckoutCardInstallmentOptionsResponse`](../../doc/models/get-checkout-card-installment-options-response.md) | Required | Parcelas |
| `authentication` | [`GetPaymentAuthenticationResponse`](../../doc/models/get-payment-authentication-response.md) | Required | Payment Authentication response |

## Example (as JSON)

```json
{
  "statementDescriptor": "statementDescriptor6",
  "installments": [
    {
      "number": "number3",
      "total": 109
    },
    {
      "number": "number4",
      "total": 110
    },
    {
      "number": "number5",
      "total": 111
    }
  ],
  "authentication": {
    "type": "type2",
    "threed_secure": {
      "mpi": "mpi6",
      "eci": "eci6",
      "cavv": "cavv2",
      "transaction_Id": "transaction_Id8",
      "success_url": "success_url8"
    }
  }
}
```

