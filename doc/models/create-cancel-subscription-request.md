
# Create Cancel Subscription Request

Request for canceling a subscription

## Structure

`CreateCancelSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cancel_pending_invoices` | `bool` | Required | Indicates if the pending invoices must also be canceled.<br><br>**Default**: `True` |

## Example

```python
from pagarmeapisdk.models.create_cancel_subscription_request import CreateCancelSubscriptionRequest

create_cancel_subscription_request = CreateCancelSubscriptionRequest(
    cancel_pending_invoices=True
)
```

