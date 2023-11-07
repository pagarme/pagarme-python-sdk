
# Create Anticipation Request

Request for creating an anticipation

## Structure

`CreateAnticipationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Amount requested for the anticipation |
| `timeframe` | `str` | Required | Timeframe |
| `payment_date` | `datetime` | Required | Payment date |

## Example (as JSON)

```json
{
  "amount": 68,
  "timeframe": "timeframe2",
  "payment_date": "2016-03-13T12:52:32.123Z"
}
```

