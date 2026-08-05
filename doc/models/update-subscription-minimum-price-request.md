
# Update Subscription Minimum Price Request

Atualização do valor mínimo da assinatura

## Structure

`UpdateSubscriptionMinimumPriceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `minimum_price` | `int` | Optional | Valor mínimo da assinatura |

## Example

```python
from pagarmeapisdk.models.update_subscription_minimum_price_request import UpdateSubscriptionMinimumPriceRequest

update_subscription_minimum_price_request = UpdateSubscriptionMinimumPriceRequest(
    minimum_price=52
)
```

