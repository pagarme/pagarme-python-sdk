
# Get Balance Response

Balance

## Structure

`GetBalanceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `string` | Optional | Currency |
| `available_amount` | `long\|int` | Optional | Amount available for transferring |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `transferred_amount` | `long\|int` | Optional | - |
| `waiting_funds_amount` | `long\|int` | Optional | - |

## Example (as JSON)

```json
{
  "currency": null,
  "available_amount": null,
  "recipient": null,
  "transferred_amount": null,
  "waiting_funds_amount": null
}
```

