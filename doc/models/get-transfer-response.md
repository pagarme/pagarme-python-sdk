
# Get Transfer Response

Transfer response

## Structure

`GetTransferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Id |
| `amount` | `int` | Optional | Transfer amount |
| `status` | `str` | Optional | Transfer status |
| `created_at` | `datetime` | Optional | Transfer creation date |
| `updated_at` | `datetime` | Optional | Transfer last update date |
| `bank_account` | [`GetBankAccountResponse`](../../doc/models/get-bank-account-response.md) | Optional | Bank account |
| `metadata` | `Dict[str, str]` | Optional | Metadata |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transfer_response import GetTransferResponse

get_transfer_response = GetTransferResponse(
    id='id2',
    amount=92,
    status='status6',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

