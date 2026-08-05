
# Update Subscription Card Request

Request for updating the card from a subscription

## Structure

`UpdateSubscriptionCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Required | Credit card data |
| `card_id` | `str` | Required | Credit card id |
| `indirect_acceptor` | `str` | Optional | Business model identifier |

## Example

```python
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.update_subscription_card_request import UpdateSubscriptionCardRequest

update_subscription_card_request = UpdateSubscriptionCardRequest(
    card=CreateCardRequest(
        number='number6',
        holder_name='holder_name2',
        exp_month=228,
        exp_year=68,
        cvv='cvv4',
        mtype='credit'
    ),
    card_id=None,
    indirect_acceptor='indirect_acceptor4'
)
```

