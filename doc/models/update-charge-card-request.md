
# Update Charge Card Request

Request for updating card data

## Structure

`UpdateChargeCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `update_subscription` | `bool` | Required | Indicates if the subscriptions using this card must also be updated |
| `card_id` | `str` | Required | Card id |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Required | Card data |
| `recurrence` | `bool` | Required | Indicates a recurrence |
| `initiated_type` | `str` | Optional | - |
| `recurrence_model` | `str` | Optional | - |
| `payment_origin` | [`CreatePaymentOriginRequest`](../../doc/models/create-payment-origin-request.md) | Optional | - |
| `indirect_acceptor` | `str` | Optional | Business model identifier |

## Example

```python
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_payment_origin_request import CreatePaymentOriginRequest
from pagarmeapisdk.models.update_charge_card_request import UpdateChargeCardRequest

update_charge_card_request = UpdateChargeCardRequest(
    update_subscription=None,
    card_id=None,
    card=CreateCardRequest(
        number='number6',
        holder_name='holder_name2',
        exp_month=228,
        exp_year=68,
        cvv='cvv4',
        mtype='credit'
    ),
    recurrence=None,
    initiated_type='initiated_type0',
    recurrence_model='recurrence_model8',
    payment_origin=CreatePaymentOriginRequest(),
    indirect_acceptor='indirect_acceptor4'
)
```

