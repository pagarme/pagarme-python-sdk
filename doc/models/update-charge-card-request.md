
# Update Charge Card Request

Request for updating card data

## Structure

`UpdateChargeCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `update_subscription` | `bool` | Required | Indicates if the subscriptions using this card must also be updated |
| `card_id` | `str` | Required | Card id |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Required | Card data |
| `recurrence` | `bool` | Required | Indicates a recurrence |
| `initiated_type` | `str` | Optional | - |
| `recurrence_model` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "update_subscription": false,
  "card_id": "card_id2",
  "card": {
    "type": "credit",
    "number": "number6",
    "holder_name": "holder_name2",
    "exp_month": 228,
    "exp_year": 68,
    "cvv": "cvv4"
  },
  "recurrence": false,
  "initiated_type": "initiated_type8",
  "recurrence_model": "recurrence_model6"
}
```

