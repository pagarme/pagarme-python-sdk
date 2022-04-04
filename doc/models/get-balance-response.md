
# Get Balance Response

Balance

## Structure

`GetBalanceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `string` | Required | Currency |
| `available_amount` | `long\|int` | Required | Amount available for transferring |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `transferred_amount` | `long\|int` | Required | - |
| `waiting_funds_amount` | `long\|int` | Required | - |

## Example (as JSON)

```json
{
  "currency": "currency0",
  "available_amount": 182,
  "recipient": null,
  "transferred_amount": 228,
  "waiting_funds_amount": 252
}
```

