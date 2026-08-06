
# Get Checkout Payment Settings Response

Checkout Payment Settings Response

## Structure

`GetCheckoutPaymentSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success_url` | `str` | Optional | Success Url |
| `payment_url` | `str` | Optional | Payment Url |
| `accepted_payment_methods` | `List[str]` | Optional | Accepted Payment Methods |
| `status` | `str` | Optional | Status |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | Customer |
| `amount` | `int` | Optional | Payment amount |
| `default_payment_method` | `str` | Optional | Default Payment Method |
| `gateway_affiliation_id` | `str` | Optional | Gateway Affiliation Id |

## Example

```python
from pagarmeapisdk.models.get_checkout_payment_settings_response import GetCheckoutPaymentSettingsResponse

get_checkout_payment_settings_response = GetCheckoutPaymentSettingsResponse(
    success_url='success_url2',
    payment_url='payment_url4',
    accepted_payment_methods=[
        'accepted_payment_methods3',
        'accepted_payment_methods4'
    ],
    status='status2',
    customer=None
)
```

