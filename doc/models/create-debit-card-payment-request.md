
# Create Debit Card Payment Request

The settings for creating a debit card payment

## Structure

`CreateDebitCardPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `string` | Optional | The text that will be shown on the debit card's statement |
| `card` | [`CreateCardRequest`](/doc/models/create-card-request.md) | Optional | Debit card data |
| `card_id` | `string` | Optional | The debit card id |
| `card_token` | `string` | Optional | The debit card token |
| `recurrence` | `bool` | Optional | Indicates a recurrence |
| `authentication` | [`CreatePaymentAuthenticationRequest`](/doc/models/create-payment-authentication-request.md) | Optional | The payment authentication request |
| `token` | [`CreateCardPaymentContactlessRequest`](/doc/models/create-card-payment-contactless-request.md) | Optional | The Debit card payment token request |

## Example (as JSON)

```json
{
  "statement_descriptor": null,
  "card": null,
  "card_id": null,
  "card_token": null,
  "recurrence": null,
  "authentication": null,
  "token": null
}
```

