
# Update Subscription Billing Date Request

Request for updating the due date from a subscription

## Structure

`UpdateSubscriptionBillingDateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next_billing_at` | `datetime` | Required | The date when the next subscription billing must occur |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.update_subscription_billing_date_request import UpdateSubscriptionBillingDateRequest

update_subscription_billing_date_request = UpdateSubscriptionBillingDateRequest(
    next_billing_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

