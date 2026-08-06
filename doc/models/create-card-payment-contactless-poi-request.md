
# Create Card Payment Contactless POI Request

## Structure

`CreateCardPaymentContactlessPOIRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `system_name` | `str` | Required | system name |
| `model` | `str` | Required | model |
| `provider` | `str` | Required | provider |
| `serial_number` | `str` | Required | serial number |
| `version_number` | `str` | Required | version number |

## Example

```python
from pagarmeapisdk.models.create_card_payment_contactless_poi_request import CreateCardPaymentContactlessPOIRequest

create_card_payment_contactless_poi_request = CreateCardPaymentContactlessPOIRequest(
    system_name='system_name8',
    model='model6',
    provider='provider0',
    serial_number='serial_number2',
    version_number='version_number2'
)
```

