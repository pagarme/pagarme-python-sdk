
# Create Checkout Payment Request

Checkout payment request

## Structure

`CreateCheckoutPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepted_payment_methods` | `List[str]` | Required | Accepted Payment Methods |
| `accepted_multi_payment_methods` | `List[Any]` | Required | Accepted Multi Payment Methods |
| `success_url` | `str` | Required | Success url |
| `default_payment_method` | `str` | Optional | Default payment method |
| `gateway_affiliation_id` | `str` | Optional | Gateway Affiliation Id |
| `credit_card` | [`CreateCheckoutCreditCardPaymentRequest`](../../doc/models/create-checkout-credit-card-payment-request.md) | Optional | Credit Card payment request |
| `debit_card` | [`CreateCheckoutDebitCardPaymentRequest`](../../doc/models/create-checkout-debit-card-payment-request.md) | Optional | Debit Card payment request |
| `boleto` | [`CreateCheckoutBoletoPaymentRequest`](../../doc/models/create-checkout-boleto-payment-request.md) | Optional | Boleto payment request |
| `customer_editable` | `bool` | Optional | Customer is editable? |
| `expires_in` | `int` | Optional | Time in minutes for expiration |
| `skip_checkout_success_page` | `bool` | Required | Skip postpay success screen? |
| `billing_address_editable` | `bool` | Required | Billing Address is editable? |
| `billing_address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | Billing Address |
| `bank_transfer` | [`CreateCheckoutBankTransferRequest`](../../doc/models/create-checkout-bank-transfer-request.md) | Optional | Bank Transfer payment request |
| `accepted_brands` | `List[str]` | Required | Accepted Brands |
| `pix` | [`CreateCheckoutPixPaymentRequest`](../../doc/models/create-checkout-pix-payment-request.md) | Optional | Pix payment request |

## Example

```python
import dateutil.parser
import jsonpickle

from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_checkout_boleto_payment_request import CreateCheckoutBoletoPaymentRequest
from pagarmeapisdk.models.create_checkout_credit_card_payment_request import CreateCheckoutCreditCardPaymentRequest
from pagarmeapisdk.models.create_checkout_debit_card_payment_request import CreateCheckoutDebitCardPaymentRequest
from pagarmeapisdk.models.create_checkout_payment_request import CreateCheckoutPaymentRequest
from pagarmeapisdk.models.create_payment_authentication_request import CreatePaymentAuthenticationRequest
from pagarmeapisdk.models.create_three_d_secure_request import CreateThreeDSecureRequest

create_checkout_payment_request = CreateCheckoutPaymentRequest(
    accepted_payment_methods=[
        'accepted_payment_methods1',
        'accepted_payment_methods2',
        'accepted_payment_methods3'
    ],
    accepted_multi_payment_methods=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    success_url='success_url0',
    skip_checkout_success_page=False,
    billing_address_editable=False,
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
    accepted_brands=[
        'accepted_brands4',
        'accepted_brands5',
        'accepted_brands6'
    ],
    default_payment_method='default_payment_method8',
    gateway_affiliation_id='gateway_affiliation_id4',
    credit_card=CreateCheckoutCreditCardPaymentRequest(),
    debit_card=CreateCheckoutDebitCardPaymentRequest(
        authentication=CreatePaymentAuthenticationRequest(
            mtype=None,
            threed_secure=CreateThreeDSecureRequest(
                mpi=None
            )
        )
    ),
    boleto=CreateCheckoutBoletoPaymentRequest(
        bank=None,
        instructions=None,
        due_at=dateutil.parser.parse(None)
    )
)
```

