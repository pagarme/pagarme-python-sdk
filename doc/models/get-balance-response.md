
# Get Balance Response

Balance

## Structure

`GetBalanceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | Currency |
| `available_amount` | `int` | Optional | Amount available for transferring |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `transferred_amount` | `int` | Optional | - |
| `waiting_funds_amount` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "currency": "currency2",
  "available_amount": 96,
  "recipient": {
    "id": "id8",
    "name": "name8",
    "email": "email8",
    "document": "document8",
    "description": "description2"
  },
  "transferred_amount": 142,
  "waiting_funds_amount": 174
}
```

