
# Get Cash Transaction Response

Response object for getting a cash transaction

## Structure

`GetCashTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Description |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transaction_response import GetCashTransactionResponse

get_cash_transaction_response = GetCashTransactionResponse(
    description='description2',
    gateway_id='gateway_id8',
    amount=40,
    status='status6',
    success=False,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

