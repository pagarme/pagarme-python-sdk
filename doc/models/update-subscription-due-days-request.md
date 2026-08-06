
# Update Subscription Due Days Request

## Structure

`UpdateSubscriptionDueDaysRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boleto_due_days` | `int` | Required | - |

## Example

```python
from pagarmeapisdk.models.update_subscription_due_days_request import UpdateSubscriptionDueDaysRequest

update_subscription_due_days_request = UpdateSubscriptionDueDaysRequest(
    boleto_due_days=166
)
```

