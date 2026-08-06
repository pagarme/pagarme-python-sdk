
# Get Transaction Report File Response

## Structure

`GetTransactionReportFileResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `date` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transaction_report_file_response import GetTransactionReportFileResponse

get_transaction_report_file_response = GetTransactionReportFileResponse(
    name='name2',
    date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

