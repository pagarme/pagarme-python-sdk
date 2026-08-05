
# Update Subscription Affiliation Id Request

Request for updating a Subscription Affiliation Id

## Structure

`UpdateSubscriptionAffiliationIdRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gateway_affiliation_id` | `str` | Required | - |

## Example

```python
from pagarmeapisdk.models.update_subscription_affiliation_id_request import UpdateSubscriptionAffiliationIdRequest

update_subscription_affiliation_id_request = UpdateSubscriptionAffiliationIdRequest(
    gateway_affiliation_id='gateway_affiliation_id6'
)
```

