
# Update Subscription Start at Request

Request for updating the start date from a subscription

## Structure

`UpdateSubscriptionStartAtRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_at` | `datetime` | Required | The date when the subscription periods will start |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.update_subscription_start_at_request import UpdateSubscriptionStartAtRequest

update_subscription_start_at_request = UpdateSubscriptionStartAtRequest(
    start_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

