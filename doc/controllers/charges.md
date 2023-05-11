# Charges

```python
charges_controller = client.charges
```

## Class Name

`ChargesController`

## Methods

* [Update Charge Metadata](../../doc/controllers/charges.md#update-charge-metadata)
* [Update Charge Payment Method](../../doc/controllers/charges.md#update-charge-payment-method)
* [Get Charge Transactions](../../doc/controllers/charges.md#get-charge-transactions)
* [Update Charge Due Date](../../doc/controllers/charges.md#update-charge-due-date)
* [Get Charges](../../doc/controllers/charges.md#get-charges)
* [Capture Charge](../../doc/controllers/charges.md#capture-charge)
* [Update Charge Card](../../doc/controllers/charges.md#update-charge-card)
* [Get Charge](../../doc/controllers/charges.md#get-charge)
* [Get Charges Summary](../../doc/controllers/charges.md#get-charges-summary)
* [Retry Charge](../../doc/controllers/charges.md#retry-charge)
* [Cancel Charge](../../doc/controllers/charges.md#cancel-charge)
* [Create Charge](../../doc/controllers/charges.md#create-charge)
* [Confirm Payment](../../doc/controllers/charges.md#confirm-payment)


# Update Charge Metadata

Updates the metadata from a charge

```python
def update_charge_metadata(self,
                          charge_id,
                          request,
                          idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | The charge id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Request for updating the charge metadata |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

request = UpdateMetadataRequest(
    metadata={
        "key0": 'metadata3'
    }
)

result = charges_controller.update_charge_metadata(
    charge_id,
    request
)
print(result)
```


# Update Charge Payment Method

Updates a charge's payment method

```python
def update_charge_payment_method(self,
                                charge_id,
                                request,
                                idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | Charge id |
| `request` | [`UpdateChargePaymentMethodRequest`](../../doc/models/update-charge-payment-method-request.md) | Body, Required | Request for updating the payment method from a charge |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

request = UpdateChargePaymentMethodRequest(
    update_subscription=False,
    payment_method='payment_method4',
    credit_card=CreateCreditCardPaymentRequest(
        installments=1,
        capture=True,
        recurrency_cycle='"first" or "subsequent"'
    ),
    debit_card=CreateDebitCardPaymentRequest(),
    boleto=CreateBoletoPaymentRequest(
        retries=10,
        bank='bank4',
        instructions='instructions4',
        billing_address=CreateAddressRequest(
            street='street8',
            number='number4',
            zip_code='zip_code2',
            neighborhood='neighborhood4',
            city='city2',
            state='state6',
            country='country2',
            complement='complement6',
            metadata={
                "key0": 'metadata5'
            },
            line_1='line_18',
            line_2='line_26'
        ),
        document_number='document_number0',
        statement_descriptor='statement_descriptor6'
    ),
    voucher=CreateVoucherPaymentRequest(
        recurrency_cycle='"first" or "subsequent"'
    ),
    cash=CreateCashPaymentRequest(
        description='description6',
        confirm=False
    ),
    bank_transfer=CreateBankTransferPaymentRequest(
        bank='bank4',
        retries=204
    ),
    private_label=CreatePrivateLabelPaymentRequest(
        installments=1,
        capture=True,
        recurrency_cycle='"first" or "subsequent"'
    )
)

result = charges_controller.update_charge_payment_method(
    charge_id,
    request
)
print(result)
```


# Get Charge Transactions

```python
def get_charge_transactions(self,
                           charge_id,
                           page=None,
                           size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | Charge Id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |

## Response Type

[`ListChargeTransactionsResponse`](../../doc/models/list-charge-transactions-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.get_charge_transactions(charge_id)
print(result)
```


# Update Charge Due Date

Updates the due date from a charge

```python
def update_charge_due_date(self,
                          charge_id,
                          request,
                          idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | Charge Id |
| `request` | [`UpdateChargeDueDateRequest`](../../doc/models/update-charge-due-date-request.md) | Body, Required | Request for updating the due date |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

request = UpdateChargeDueDateRequest()

result = charges_controller.update_charge_due_date(
    charge_id,
    request
)
print(result)
```


# Get Charges

Lists all charges

```python
def get_charges(self,
               page=None,
               size=None,
               code=None,
               status=None,
               payment_method=None,
               customer_id=None,
               order_id=None,
               created_since=None,
               created_until=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `code` | `string` | Query, Optional | Filter for charge's code |
| `status` | `string` | Query, Optional | Filter for charge's status |
| `payment_method` | `string` | Query, Optional | Filter for charge's payment method |
| `customer_id` | `string` | Query, Optional | Filter for charge's customer id |
| `order_id` | `string` | Query, Optional | Filter for charge's order id |
| `created_since` | `datetime` | Query, Optional | Filter for the beginning of the range for charge's creation |
| `created_until` | `datetime` | Query, Optional | Filter for the end of the range for charge's creation |

## Response Type

[`ListChargesResponse`](../../doc/models/list-charges-response.md)

## Example Usage

```python
result = charges_controller.get_charges()
print(result)
```


# Capture Charge

Captures a charge

```python
def capture_charge(self,
                  charge_id,
                  request=None,
                  idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | Charge id |
| `request` | [`CreateCaptureChargeRequest`](../../doc/models/create-capture-charge-request.md) | Body, Optional | Request for capturing a charge |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.capture_charge(charge_id)
print(result)
```


# Update Charge Card

Updates the card from a charge

```python
def update_charge_card(self,
                      charge_id,
                      request,
                      idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | Charge id |
| `request` | [`UpdateChargeCardRequest`](../../doc/models/update-charge-card-request.md) | Body, Required | Request for updating a charge's card |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

request = UpdateChargeCardRequest(
    update_subscription=False,
    card_id='card_id2',
    card=CreateCardRequest(
        mtype='credit'
    ),
    recurrence=False
)

result = charges_controller.update_charge_card(
    charge_id,
    request
)
print(result)
```


# Get Charge

Get a charge from its id

```python
def get_charge(self,
              charge_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | Charge id |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.get_charge(charge_id)
print(result)
```


# Get Charges Summary

```python
def get_charges_summary(self,
                       status,
                       created_since=None,
                       created_until=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `string` | Query, Required | - |
| `created_since` | `datetime` | Query, Optional | - |
| `created_until` | `datetime` | Query, Optional | - |

## Response Type

[`GetChargesSummaryResponse`](../../doc/models/get-charges-summary-response.md)

## Example Usage

```python
status = 'status8'

result = charges_controller.get_charges_summary(status)
print(result)
```


# Retry Charge

Retries a charge

```python
def retry_charge(self,
                charge_id,
                idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | Charge id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.retry_charge(charge_id)
print(result)
```


# Cancel Charge

Cancel a charge

```python
def cancel_charge(self,
                 charge_id,
                 request=None,
                 idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | Charge id |
| `request` | [`CreateCancelChargeRequest`](../../doc/models/create-cancel-charge-request.md) | Body, Optional | Request for cancelling a charge |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.cancel_charge(charge_id)
print(result)
```


# Create Charge

Creates a new charge

```python
def create_charge(self,
                 request,
                 idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`CreateChargeRequest`](../../doc/models/create-charge-request.md) | Body, Required | Request for creating a charge |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
request = CreateChargeRequest(
    amount=242,
    payment=CreatePaymentRequest(
        payment_method='payment_method2'
    ),
    order_id='order_id0'
)

result = charges_controller.create_charge(request)
print(result)
```


# Confirm Payment

```python
def confirm_payment(self,
                   charge_id,
                   request=None,
                   idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `string` | Template, Required | - |
| `request` | [`CreateConfirmPaymentRequest`](../../doc/models/create-confirm-payment-request.md) | Body, Optional | Request for confirm payment |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](../../doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.confirm_payment(charge_id)
print(result)
```

