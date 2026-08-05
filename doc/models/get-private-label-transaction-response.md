
# Get Private Label Transaction Response

Response object for getting a private label transaction

## Structure

`GetPrivateLabelTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | Text that will appear on the credit card's statement |
| `acquirer_name` | `str` | Optional | Acquirer name |
| `acquirer_affiliation_code` | `str` | Optional | Aquirer affiliation code |
| `acquirer_tid` | `str` | Optional | Acquirer TID |
| `acquirer_nsu` | `str` | Optional | Acquirer NSU |
| `acquirer_auth_code` | `str` | Optional | Acquirer authorization code |
| `operation_type` | `str` | Optional | Operation type |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | Card data |
| `acquirer_message` | `str` | Optional | Acquirer message |
| `acquirer_return_code` | `str` | Optional | Acquirer Return Code |
| `installments` | `int` | Optional | Number of installments |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transaction_response import GetPrivateLabelTransactionResponse

get_private_label_transaction_response = GetPrivateLabelTransactionResponse(
    statement_descriptor='statement_descriptor0',
    acquirer_name='acquirer_name4',
    acquirer_affiliation_code='acquirer_affiliation_code2',
    acquirer_tid='acquirer_tid0',
    acquirer_nsu='acquirer_nsu0',
    gateway_id='gateway_id8',
    amount=40,
    status='status6',
    success=False,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

