
# Create Private Label Payment Request

The settings for creating a private label payment

## Structure

`CreatePrivateLabelPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `installments` | `int` | Optional | Number of installments<br><br>**Default**: `1` |
| `statement_descriptor` | `str` | Optional | The text that will be shown on the private label's statement |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Optional | Card data |
| `card_id` | `str` | Optional | The Card id |
| `card_token` | `str` | Optional | - |
| `recurrence` | `bool` | Optional | Indicates a recurrence |
| `capture` | `bool` | Optional | Indicates if the operation should be only authorization or auth and capture.<br><br>**Default**: `True` |
| `extended_limit_enabled` | `bool` | Optional | Indicates whether the extended label (private label) is enabled |
| `extended_limit_code` | `str` | Optional | Extended Limit Code |
| `recurrency_cycle` | `str` | Optional | Defines whether the card has been used one or more times. |

## Example (as JSON)

```json
{
  "installments": 1,
  "capture": true,
  "recurrency_cycle": "\"first\" or \"subsequent\"",
  "statement_descriptor": "statement_descriptor8",
  "card": {
    "number": "number6",
    "holder_name": "holder_name2",
    "exp_month": 228,
    "exp_year": 68,
    "cvv": "cvv4"
  },
  "card_id": "card_id4",
  "card_token": "card_token2"
}
```

