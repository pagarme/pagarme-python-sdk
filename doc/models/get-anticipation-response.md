
# Get Anticipation Response

Anticipation

## Structure

`GetAnticipationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Id |
| `requested_amount` | `int` | Optional | Requested amount |
| `approved_amount` | `int` | Optional | Approved amount |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `pgid` | `str` | Optional | Anticipation id on the gateway |
| `created_at` | `datetime` | Optional | Creation date |
| `updated_at` | `datetime` | Optional | Last update date |
| `payment_date` | `datetime` | Optional | Payment date |
| `status` | `str` | Optional | Status |
| `timeframe` | `str` | Optional | Timeframe |

## Example (as JSON)

```json
{
  "id": "id8",
  "requested_amount": 130,
  "approved_amount": 184,
  "recipient": {
    "id": "id8",
    "name": "name8",
    "email": "email8",
    "document": "document8",
    "description": "description2"
  },
  "pgid": "pgid4"
}
```

