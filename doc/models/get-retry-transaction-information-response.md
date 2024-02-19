
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

## Example (as JSON)

```json
{
  "brand_failure_return_code": "brand_failure_return_code2",
  "transaction_limit": 44,
  "transaction_date_limit": "2016-03-13T12:52:32.123Z"
}
```

