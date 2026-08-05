
# Update Subscription Payment Method Request

Request for updating a subscription's payment method

## Structure

`UpdateSubscriptionPaymentMethodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_method` | `str` | Required | The new payment method |
| `card_id` | `str` | Required | Card id |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Required | Card data |
| `card_token` | `str` | Optional | The Card Token |
| `boleto` | [`CreateSubscriptionBoletoRequest`](../../doc/models/create-subscription-boleto-request.md) | Optional | Information about fines and interest on the "boleto" used from payment |
| `indirect_acceptor` | `str` | Optional | Business model identifier |

## Example

```python
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_subscription_boleto_request import CreateSubscriptionBoletoRequest
from pagarmeapisdk.models.update_subscription_payment_method_request import UpdateSubscriptionPaymentMethodRequest

update_subscription_payment_method_request = UpdateSubscriptionPaymentMethodRequest(
    payment_method=None,
    card_id=None,
    card=CreateCardRequest(
        number='number6',
        holder_name='holder_name2',
        exp_month=228,
        exp_year=68,
        cvv='cvv4',
        mtype='credit'
    ),
    card_token='card_token8',
    boleto=CreateSubscriptionBoletoRequest(),
    indirect_acceptor='indirect_acceptor8'
)
```

