
# Create Pix Payment Request

Contains information to create a pix payment

## Structure

`CreatePixPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_at` | `datetime` | Optional | Datetime when pix payment will expire |
| `expires_in` | `int` | Optional | Seconds until pix payment expires |
| `additional_information` | [`List[PixAdditionalInformation]`](../../doc/models/pix-additional-information.md) | Optional | Pix additional information |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_pix_payment_request import CreatePixPaymentRequest
from pagarmeapisdk.models.pix_additional_information import PixAdditionalInformation

create_pix_payment_request = CreatePixPaymentRequest(
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expires_in=136,
    additional_information=[
        None,
        PixAdditionalInformation(),
        PixAdditionalInformation()
    ]
)
```

