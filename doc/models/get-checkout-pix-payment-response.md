
# Get Checkout Pix Payment Response

Checkout pix payment response

## Structure

`GetCheckoutPixPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_at` | `datetime` | Optional | Expires at |
| `additional_information` | [`List[PixAdditionalInformation]`](../../doc/models/pix-additional-information.md) | Optional | Additional information |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_checkout_pix_payment_response import GetCheckoutPixPaymentResponse
from pagarmeapisdk.models.pix_additional_information import PixAdditionalInformation

get_checkout_pix_payment_response = GetCheckoutPixPaymentResponse(
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_information=[
        None,
        PixAdditionalInformation(),
        PixAdditionalInformation()
    ]
)
```

