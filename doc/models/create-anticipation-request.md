
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

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_anticipation_request import CreateAnticipationRequest

create_anticipation_request = CreateAnticipationRequest(
    amount=40,
    timeframe='timeframe2',
    payment_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

