
# Update Current Cycle End Date Request

Request to update the end date of the current subscription cycle

## Structure

`UpdateCurrentCycleEndDateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_at` | `datetime` | Optional | Current cycle end date |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.update_current_cycle_end_date_request import UpdateCurrentCycleEndDateRequest

update_current_cycle_end_date_request = UpdateCurrentCycleEndDateRequest(
    end_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

