
# Update Charge Payment Method Request

Request for updating the payment method of a charge

## Structure

`UpdateChargePaymentMethodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `update_subscription` | `bool` | Required | Indicates if the payment method from the subscription must also be updated |
| `payment_method` | `str` | Required | The new payment method |
| `credit_card` | [`CreateCreditCardPaymentRequest`](../../doc/models/create-credit-card-payment-request.md) | Required | Credit card data |
| `debit_card` | [`CreateDebitCardPaymentRequest`](../../doc/models/create-debit-card-payment-request.md) | Required | Debit card data |
| `boleto` | [`CreateBoletoPaymentRequest`](../../doc/models/create-boleto-payment-request.md) | Required | Boleto data |
| `voucher` | [`CreateVoucherPaymentRequest`](../../doc/models/create-voucher-payment-request.md) | Required | Voucher data |
| `cash` | [`CreateCashPaymentRequest`](../../doc/models/create-cash-payment-request.md) | Required | Cash data |
| `bank_transfer` | [`CreateBankTransferPaymentRequest`](../../doc/models/create-bank-transfer-payment-request.md) | Required | Bank Transfer data |
| `private_label` | [`CreatePrivateLabelPaymentRequest`](../../doc/models/create-private-label-payment-request.md) | Required | - |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_bank_transfer_payment_request import CreateBankTransferPaymentRequest
from pagarmeapisdk.models.create_boleto_payment_request import CreateBoletoPaymentRequest
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_cash_payment_request import CreateCashPaymentRequest
from pagarmeapisdk.models.create_credit_card_payment_request import CreateCreditCardPaymentRequest
from pagarmeapisdk.models.create_debit_card_payment_request import CreateDebitCardPaymentRequest
from pagarmeapisdk.models.create_private_label_payment_request import CreatePrivateLabelPaymentRequest
from pagarmeapisdk.models.create_voucher_payment_request import CreateVoucherPaymentRequest
from pagarmeapisdk.models.update_charge_payment_method_request import UpdateChargePaymentMethodRequest

update_charge_payment_method_request = UpdateChargePaymentMethodRequest(
    update_subscription=None,
    payment_method=None,
    credit_card=CreateCreditCardPaymentRequest(
        installments=1,
        statement_descriptor='statement_descriptor8',
        card=CreateCardRequest(),
        card_id='card_id4',
        card_token='card_token2',
        capture=True,
        recurrency_cycle='"first" or "subsequent"'
    ),
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
    voucher=CreateVoucherPaymentRequest(
        statement_descriptor='statement_descriptor2',
        card_id='card_id8',
        card_token='card_token8',
        card=CreateCardRequest(),
        recurrency_cycle='"first" or "subsequent"'
    ),
    cash=CreateCashPaymentRequest(
        description=None,
        confirm=None
    ),
    bank_transfer=CreateBankTransferPaymentRequest(
        bank=None,
        retries=None
    ),
    private_label=CreatePrivateLabelPaymentRequest(
        installments=1,
        statement_descriptor='statement_descriptor0',
        card=CreateCardRequest(),
        card_id='card_id6',
        card_token='card_token0',
        capture=True,
        recurrency_cycle='"first" or "subsequent"'
    )
)
```

