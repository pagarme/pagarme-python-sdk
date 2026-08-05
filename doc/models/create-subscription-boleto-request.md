
# Create Subscription Boleto Request

Information about fines and interest on the "boleto" used from payment

## Structure

`CreateSubscriptionBoletoRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interest` | [`CreateInterestRequest`](../../doc/models/create-interest-request.md) | Optional | - |
| `fine` | [`CreateFineRequest`](../../doc/models/create-fine-request.md) | Optional | - |
| `max_days_to_pay_past_due` | `int` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_fine_request import CreateFineRequest
from pagarmeapisdk.models.create_interest_request import CreateInterestRequest
from pagarmeapisdk.models.create_subscription_boleto_request import CreateSubscriptionBoletoRequest

create_subscription_boleto_request = CreateSubscriptionBoletoRequest(
    interest=CreateInterestRequest(
        days=None,
        mtype=None,
        amount=None
    ),
    fine=CreateFineRequest(
        days=None,
        mtype=None,
        amount=None
    ),
    max_days_to_pay_past_due=228
)
```

