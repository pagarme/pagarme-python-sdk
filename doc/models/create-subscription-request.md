
# Create Subscription Request

Request for creating a subcription

## Structure

`CreateSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer` | [`CreateCustomerRequest`](../../doc/models/create-customer-request.md) | Required | Customer |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Required | Card |
| `code` | `str` | Required | Subscription code |
| `payment_method` | `str` | Required | Payment method |
| `billing_type` | `str` | Required | Billing type |
| `statement_descriptor` | `str` | Required | Statement descriptor for credit card subscriptions |
| `description` | `str` | Required | Subscription description |
| `currency` | `str` | Required | Currency |
| `interval` | `str` | Required | Interval |
| `interval_count` | `int` | Required | Interval count |
| `pricing_scheme` | [`CreatePricingSchemeRequest`](../../doc/models/create-pricing-scheme-request.md) | Required | Subscription pricing scheme |
| `items` | [`List[CreateSubscriptionItemRequest]`](../../doc/models/create-subscription-item-request.md) | Required | Subscription items |
| `shipping` | [`CreateShippingRequest`](../../doc/models/create-shipping-request.md) | Required | Shipping |
| `discounts` | [`List[CreateDiscountRequest]`](../../doc/models/create-discount-request.md) | Required | Discounts |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `setup` | [`CreateSetupRequest`](../../doc/models/create-setup-request.md) | Optional | Setup data |
| `plan_id` | `str` | Optional | Plan id |
| `customer_id` | `str` | Optional | Customer id |
| `card_id` | `str` | Optional | Card id |
| `billing_day` | `int` | Optional | Billing day |
| `installments` | `int` | Optional | Number of installments |
| `start_at` | `datetime` | Optional | Subscription start date |
| `minimum_price` | `int` | Optional | Subscription minimum price |
| `cycles` | `int` | Optional | Number of cycles |
| `card_token` | `str` | Optional | Card token |
| `gateway_affiliation_id` | `str` | Optional | Gateway Affiliation code |
| `quantity` | `int` | Optional | Quantity |
| `boleto_due_days` | `int` | Optional | Days until boleto expires |
| `increments` | [`List[CreateIncrementRequest]`](../../doc/models/create-increment-request.md) | Required | Increments |
| `period` | [`CreatePeriodRequest`](../../doc/models/create-period-request.md) | Optional | - |
| `submerchant` | [`CreateSubMerchantRequest`](../../doc/models/create-sub-merchant-request.md) | Optional | SubMerchant |
| `split` | [`CreateSubscriptionSplitRequest`](../../doc/models/create-subscription-split-request.md) | Optional | Subscription's split |
| `boleto` | [`CreateSubscriptionBoletoRequest`](../../doc/models/create-subscription-boleto-request.md) | Optional | Information about fines and interest on the "boleto" used from payment |
| `indirect_acceptor` | `str` | Optional | Business model identifier |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_customer_request import CreateCustomerRequest
from pagarmeapisdk.models.create_payment_request import CreatePaymentRequest
from pagarmeapisdk.models.create_phones_request import CreatePhonesRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest
from pagarmeapisdk.models.create_setup_request import CreateSetupRequest
from pagarmeapisdk.models.create_shipping_request import CreateShippingRequest
from pagarmeapisdk.models.create_subscription_item_request import CreateSubscriptionItemRequest
from pagarmeapisdk.models.create_subscription_request import CreateSubscriptionRequest

create_subscription_request = CreateSubscriptionRequest(
    customer=CreateCustomerRequest(
        name='Tony Stark',
        email=None,
        document=None,
        mtype=None,
        address=CreateAddressRequest(
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
        metadata={},
        phones=CreatePhonesRequest(),
        code=None,
        gender='gender6',
        document_type='document_type8'
    ),
    card=CreateCardRequest(
        number='number6',
        holder_name='holder_name2',
        exp_month=228,
        exp_year=68,
        cvv='cvv4',
        mtype='credit'
    ),
    code=None,
    payment_method=None,
    billing_type=None,
    statement_descriptor=None,
    description=None,
    currency=None,
    interval=None,
    interval_count=None,
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type=None
    ),
    items=[
        CreateSubscriptionItemRequest(
            description=None,
            pricing_scheme=CreatePricingSchemeRequest(
                scheme_type=None
            ),
            id=None,
            plan_item_id=None,
            discounts=[
                None
            ],
            name=None,
            cycles=214,
            quantity=22,
            minimum_price=222
        )
    ],
    shipping=CreateShippingRequest(
        amount=None,
        description=None,
        recipient_name=None,
        recipient_phone=None,
        address_id=None,
        address=CreateAddressRequest(
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
        mtype=None
    ),
    discounts=[
        None
    ],
    metadata={},
    increments=[
        None
    ],
    setup=CreateSetupRequest(
        amount=None,
        description=None,
        payment=CreatePaymentRequest(
            payment_method=None
        )
    ),
    plan_id='plan_id6',
    customer_id='customer_id2',
    card_id='card_id0',
    billing_day=242
)
```

