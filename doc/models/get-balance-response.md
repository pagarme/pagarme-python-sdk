
# Get Balance Response

Balance

## Structure

`GetBalanceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | Currency (official ISO 4217 currency names) |
| `available_amount` | `int` | Optional | Amount available for transferring in cents |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `transferred_amount` | `int` | Optional | Amount transfered in cents |
| `waiting_funds_amount` | `int` | Optional | Amount waiting in cents |
| `payment_profile_id` | `str` | Required | Operational id of merchant in payments operations (new) |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_balance_response import GetBalanceResponse
from pagarmeapisdk.models.get_recipient_response import GetRecipientResponse

get_balance_response = GetBalanceResponse(
    payment_profile_id='pp_abcdefghoj20klmn09k',
    currency='BRL',
    available_amount=4996,
    recipient=GetRecipientResponse(
        id='re_abcdefghoj20klmn09k',
        name='Lojista Recebedor LTDA',
        email='email@stone.com.br',
        document='01032644222100',
        description=None,
        mtype=None,
        status='active',
        created_at=dateutil.parser.parse('2026-06-22T19:13:52Z'),
        updated_at=None,
        deleted_at=None,
        code=None,
        payment_mode=None
    ),
    transferred_amount=None,
    waiting_funds_amount=0
)
```

