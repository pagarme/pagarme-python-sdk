
# Create Credit Card Payment Request

The settings for creating a credit card payment

## Structure

`CreateCreditCardPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `installments` | `int` | Optional | Number of installments<br>**Default**: `1` |
| `statement_descriptor` | `string` | Optional | The text that will be shown on the credit card's statement |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Optional | Credit card data |
| `card_id` | `string` | Optional | The credit card id |
| `card_token` | `string` | Optional | - |
| `recurrence` | `bool` | Optional | Indicates a recurrence |
| `capture` | `bool` | Optional | Indicates if the operation should be only authorization or auth and capture.<br>**Default**: `True` |
| `extended_limit_enabled` | `bool` | Optional | Indicates whether the extended label (private label) is enabled |
| `extended_limit_code` | `string` | Optional | Extended Limit Code |
| `merchant_category_code` | `long\|int` | Optional | Customer business segment code |
| `authentication` | [`CreatePaymentAuthenticationRequest`](../../doc/models/create-payment-authentication-request.md) | Optional | The payment authentication request |
| `contactless` | [`CreateCardPaymentContactlessRequest`](../../doc/models/create-card-payment-contactless-request.md) | Optional | The Credit card payment contactless request |
| `auto_recovery` | `bool` | Optional | Indicates whether a particular payment will enter the offline retry flow |
| `operation_type` | `string` | Optional | AuthOnly, AuthAndCapture, PreAuth |
| `recurrency_cycle` | `string` | Optional | Defines whether the card has been used one or more times. |

## Example (as JSON)

```json
{
  "installments": null,
  "statement_descriptor": null,
  "card": null,
  "card_id": null,
  "card_token": null,
  "recurrence": null,
  "capture": null,
  "extended_limit_enabled": null,
  "extended_limit_code": null,
  "merchant_category_code": null,
  "authentication": null,
  "contactless": null,
  "auto_recovery": null,
  "operation_type": null,
  "recurrency_cycle": null
}
```

