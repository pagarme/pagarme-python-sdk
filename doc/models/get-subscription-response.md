
# Get Subscription Response

## Structure

`GetSubscriptionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `start_at` | `datetime` | Optional | - |
| `interval` | `str` | Optional | - |
| `interval_count` | `int` | Optional | - |
| `billing_type` | `str` | Optional | - |
| `current_cycle` | [`GetPeriodResponse`](../../doc/models/get-period-response.md) | Optional | - |
| `payment_method` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `installments` | `int` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | - |
| `items` | [`List[GetSubscriptionItemResponse]`](../../doc/models/get-subscription-item-response.md) | Optional | - |
| `statement_descriptor` | `str` | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `setup` | [`GetSetupResponse`](../../doc/models/get-setup-response.md) | Optional | - |
| `gateway_affiliation_id` | `str` | Optional | Affiliation Code |
| `next_billing_at` | `datetime` | Optional | - |
| `billing_day` | `int` | Optional | - |
| `minimum_price` | `int` | Optional | - |
| `canceled_at` | `datetime` | Optional | - |
| `discounts` | [`List[GetDiscountResponse]`](../../doc/models/get-discount-response.md) | Optional | Subscription discounts |
| `increments` | [`List[GetIncrementResponse]`](../../doc/models/get-increment-response.md) | Optional | Subscription increments |
| `boleto_due_days` | `int` | Optional | Days until boleto expires |
| `split` | [`GetSubscriptionSplitResponse`](../../doc/models/get-subscription-split-response.md) | Optional | Subscription's split response |
| `boleto` | [`GetSubscriptionBoletoResponse`](../../doc/models/get-subscription-boleto-response.md) | Optional | - |
| `manual_billing` | `bool` | Optional | - |
| `indirect_acceptor` | `str` | Optional | Business model identifier |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_fine_response import GetFineResponse
from pagarmeapisdk.models.get_interest_response import GetInterestResponse
from pagarmeapisdk.models.get_subscription_boleto_response import GetSubscriptionBoletoResponse
from pagarmeapisdk.models.get_subscription_response import GetSubscriptionResponse

get_subscription_response = GetSubscriptionResponse(
    id='id0',
    code='code8',
    start_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    interval='interval8',
    interval_count=54,
    boleto=GetSubscriptionBoletoResponse(
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
)
```

