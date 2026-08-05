
# Get Safety Pay Transaction Response

Response object for getting a safety pay transaction

## Structure

`GetSafetyPayTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Payment url |
| `bank_tid` | `str` | Optional | Transaction identifier on bank |
| `paid_at` | `datetime` | Optional | Payment date |
| `paid_amount` | `int` | Optional | Paid amount |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transaction_response import GetSafetyPayTransactionResponse

get_safety_pay_transaction_response = GetSafetyPayTransactionResponse(
    url='url8',
    bank_tid='bank_tid8',
    paid_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    paid_amount=68,
    gateway_id='gateway_id8',
    amount=40,
    status='status6',
    success=False,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

