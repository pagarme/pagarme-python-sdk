
# Create Payment Request

Payment data

## Structure

`CreatePaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_method` | `str` | Required | Payment method |
| `credit_card` | [`CreateCreditCardPaymentRequest`](../../doc/models/create-credit-card-payment-request.md) | Optional | Settings for credit card payment |
| `debit_card` | [`CreateDebitCardPaymentRequest`](../../doc/models/create-debit-card-payment-request.md) | Optional | Settings for debit card payment |
| `boleto` | [`CreateBoletoPaymentRequest`](../../doc/models/create-boleto-payment-request.md) | Optional | Settings for boleto payment |
| `currency` | `str` | Optional | Currency. Must be informed using 3 characters |
| `voucher` | [`CreateVoucherPaymentRequest`](../../doc/models/create-voucher-payment-request.md) | Optional | Settings for voucher payment |
| `split` | [`List[CreateSplitRequest]`](../../doc/models/create-split-request.md) | Optional | Splits |
| `bank_transfer` | [`CreateBankTransferPaymentRequest`](../../doc/models/create-bank-transfer-payment-request.md) | Optional | Settings for bank transfer payment |
| `gateway_affiliation_id` | `str` | Optional | Gateway affiliation code |
| `amount` | `int` | Optional | The amount of the payment, in cents |
| `checkout` | [`CreateCheckoutPaymentRequest`](../../doc/models/create-checkout-payment-request.md) | Optional | Settings for checkout payment |
| `customer_id` | `str` | Optional | Customer Id |
| `customer` | [`CreateCustomerRequest`](../../doc/models/create-customer-request.md) | Optional | Customer |
| `metadata` | `Dict[str, str]` | Optional | Metadata |
| `cash` | [`CreateCashPaymentRequest`](../../doc/models/create-cash-payment-request.md) | Optional | Settings for cash payment |
| `private_label` | [`CreatePrivateLabelPaymentRequest`](../../doc/models/create-private-label-payment-request.md) | Optional | Settings for private label payment |
| `pix` | [`CreatePixPaymentRequest`](../../doc/models/create-pix-payment-request.md) | Optional | Settings for pix payment |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_boleto_payment_request import CreateBoletoPaymentRequest
from pagarmeapisdk.models.create_credit_card_payment_request import CreateCreditCardPaymentRequest
from pagarmeapisdk.models.create_debit_card_payment_request import CreateDebitCardPaymentRequest
from pagarmeapisdk.models.create_payment_request import CreatePaymentRequest
from pagarmeapisdk.models.create_voucher_payment_request import CreateVoucherPaymentRequest

create_payment_request = CreatePaymentRequest(
    payment_method='payment_method8',
    credit_card=CreateCreditCardPaymentRequest(),
    debit_card=CreateDebitCardPaymentRequest(),
    boleto=CreateBoletoPaymentRequest(
        retries=None,
        instructions=None,
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
        document_number=None,
        statement_descriptor=None
    ),
    currency='currency8',
    voucher=CreateVoucherPaymentRequest()
)
```

