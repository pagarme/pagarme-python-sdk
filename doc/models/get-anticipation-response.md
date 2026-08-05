
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

## Example

```python
from pagarmeapisdk.models.get_anticipation_response import GetAnticipationResponse

get_anticipation_response = GetAnticipationResponse(
    id='id8',
    requested_amount=158,
    approved_amount=212,
    recipient=None,
    pgid='pgid4'
)
```

