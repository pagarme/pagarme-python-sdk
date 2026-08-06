
# Create Voucher Payment Request

The settings for creating a voucher payment

## Structure

`CreateVoucherPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | The text that will be shown on the voucher's statement |
| `card_id` | `str` | Optional | Card id |
| `card_token` | `str` | Optional | Card token |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Optional | Card info |
| `recurrency_cycle` | `str` | Optional | Defines whether the card has been used one or more times. |

## Example

```python
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_voucher_payment_request import CreateVoucherPaymentRequest

create_voucher_payment_request = CreateVoucherPaymentRequest(
    statement_descriptor='statement_descriptor4',
    card_id='card_id0',
    card_token='card_token6',
    card=CreateCardRequest(),
    recurrency_cycle='"first" or "subsequent"'
)
```

