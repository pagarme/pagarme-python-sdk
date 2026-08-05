
# Get Retry Transaction Information Response

Response object for getting an RetryTransactionInformation

## Structure

`GetRetryTransactionInformationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_failure_return_code` | `str` | Required | - |
| `transaction_limit` | `int` | Required | - |
| `transaction_date_limit` | `datetime` | Required | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_retry_transaction_information_response import GetRetryTransactionInformationResponse

get_retry_transaction_information_response = GetRetryTransactionInformationResponse(
    brand_failure_return_code='brand_failure_return_code8',
    transaction_limit=212,
    transaction_date_limit=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

