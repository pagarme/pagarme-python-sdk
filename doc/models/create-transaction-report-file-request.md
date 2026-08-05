
# Create Transaction Report File Request

## Structure

`CreateTransactionReportFileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `start_at` | `datetime` | Optional | - |
| `end_at` | `str` | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_transaction_report_file_request import CreateTransactionReportFileRequest

create_transaction_report_file_request = CreateTransactionReportFileRequest(
    name='name8',
    start_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    end_at='end_at2'
)
```

