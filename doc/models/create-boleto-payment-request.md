
# Create Boleto Payment Request

Contains the settings for creating a boleto payment

## Structure

`CreateBoletoPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `retries` | `int` | Required | Number of retries |
| `bank` | `str` | Optional | The bank code, containing three characters. The available codes are on the API specification |
| `instructions` | `str` | Required | The instructions field that will be printed on the boleto. |
| `due_at` | `datetime` | Optional | Boleto due date |
| `billing_address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | Card's billing address |
| `billing_address_id` | `str` | Optional | The address id for the billing address |
| `nosso_numero` | `str` | Optional | Customer identification number with the bank |
| `document_number` | `str` | Required | Boleto identification |
| `statement_descriptor` | `str` | Required | Soft Descriptor |
| `interest` | [`CreateInterestRequest`](../../doc/models/create-interest-request.md) | Optional | - |
| `fine` | [`CreateFineRequest`](../../doc/models/create-fine-request.md) | Optional | - |
| `max_days_to_pay_past_due` | `int` | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_boleto_payment_request import CreateBoletoPaymentRequest

create_boleto_payment_request = CreateBoletoPaymentRequest(
    retries=42,
    instructions='instructions8',
    billing_address=CreateAddressRequest(
        street=None,
        number=None,
        zip_code=None,
        neighborhood=None,
        city=None,
        state=None,
        country=None,
        complement=None,
        line_1=None,
        line_2=None
    ),
    document_number='document_number2',
    statement_descriptor='statement_descriptor4',
    bank='bank2',
    due_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    billing_address_id='billing_address_id0',
    nosso_numero='nosso_numero4',
    interest=None
)
```

