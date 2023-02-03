
# Get Checkout Credit Card Payment Response

## Structure

`GetCheckoutCreditCardPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `string` | Optional | Descrição na fatura |
| `installments` | [`List of GetCheckoutCardInstallmentOptionsResponse`](../../doc/models/get-checkout-card-installment-options-response.md) | Optional | Parcelas |
| `authentication` | [`GetPaymentAuthenticationResponse`](../../doc/models/get-payment-authentication-response.md) | Optional | Payment Authentication response |

## Example (as JSON)

```json
{
  "statementDescriptor": null,
  "installments": null,
  "authentication": null
}
```

