
# Get Voucher Transaction Response

Response for voucher transactions

## Structure

`GetVoucherTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | Text that will appear on the voucher's statement |
| `acquirer_name` | `str` | Optional | Acquirer name |
| `acquirer_affiliation_code` | `str` | Optional | Acquirer affiliation code |
| `acquirer_tid` | `str` | Optional | Acquirer TID |
| `acquirer_nsu` | `str` | Optional | Acquirer NSU |
| `acquirer_auth_code` | `str` | Optional | Acquirer authorization code |
| `acquirer_message` | `str` | Optional | acquirer_message |
| `acquirer_return_code` | `str` | Optional | Acquirer return code |
| `operation_type` | `str` | Optional | Operation type |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | Card data |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transaction_response import GetVoucherTransactionResponse

get_voucher_transaction_response = GetVoucherTransactionResponse(
    statement_descriptor='statement_descriptor8',
    acquirer_name='acquirer_name2',
    acquirer_affiliation_code='acquirer_affiliation_code0',
    acquirer_tid='acquirer_tid2',
    acquirer_nsu='acquirer_nsu2',
    gateway_id='gateway_id8',
    amount=40,
    status='status6',
    success=False,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

