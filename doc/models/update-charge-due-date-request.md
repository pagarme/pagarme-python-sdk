
# Update Charge Due Date Request

Request for updating a charge due date

## Structure

`UpdateChargeDueDateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `due_at` | `datetime` | Optional | The charge's new due date |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.update_charge_due_date_request import UpdateChargeDueDateRequest

update_charge_due_date_request = UpdateChargeDueDateRequest(
    due_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

