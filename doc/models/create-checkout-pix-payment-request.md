
# Create Checkout Pix Payment Request

Checkout pix payment request

## Structure

`CreateCheckoutPixPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_at` | `datetime` | Optional | Expires at |
| `expires_in` | `int` | Optional | Expires in |
| `additional_information` | [`List[PixAdditionalInformation]`](../../doc/models/pix-additional-information.md) | Optional | Additional information |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_checkout_pix_payment_request import CreateCheckoutPixPaymentRequest

create_checkout_pix_payment_request = CreateCheckoutPixPaymentRequest(
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expires_in=184,
    additional_information=[
        None
    ]
)
```

