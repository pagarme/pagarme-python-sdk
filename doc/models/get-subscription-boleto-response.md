
# Get Subscription Boleto Response

Response object for getting a boleto

## Structure

`GetSubscriptionBoletoResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interest` | [`GetInterestResponse`](../../doc/models/get-interest-response.md) | Optional | Interest |
| `fine` | [`GetFineResponse`](../../doc/models/get-fine-response.md) | Optional | Fine |
| `max_days_to_pay_past_due` | `int` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_fine_response import GetFineResponse
from pagarmeapisdk.models.get_interest_response import GetInterestResponse
from pagarmeapisdk.models.get_subscription_boleto_response import GetSubscriptionBoletoResponse

get_subscription_boleto_response = GetSubscriptionBoletoResponse(
    interest=GetInterestResponse(
        days=2,
        mtype='percentage',
        amount=20
    ),
    fine=GetFineResponse(
        days=2,
        mtype='flat',
        amount=10
    ),
    max_days_to_pay_past_due=2
)
```

