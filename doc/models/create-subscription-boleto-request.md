
# Create Subscription Boleto Request

Information about fines and interest on the "boleto" used from payment

## Structure

`CreateSubscriptionBoletoRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interest` | [`CreateInterestRequest`](../../doc/models/create-interest-request.md) | Optional | - |
| `fine` | [`CreateFineRequest`](../../doc/models/create-fine-request.md) | Optional | - |
| `max_days_to_pay_past_due` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "interest": {
    "days": 156,
    "type": "type0",
    "amount": 230
  },
  "fine": {
    "days": 138,
    "type": "type2",
    "amount": 212
  },
  "max_days_to_pay_past_due": 122
}
```

