# Charges

```python
charges_controller = client.charges
```

## Class Name

`ChargesController`

## Methods

* [Update Charge Metadata](/doc/controllers/charges.md#update-charge-metadata)
* [Update Charge Payment Method](/doc/controllers/charges.md#update-charge-payment-method)
* [Get Charge Transactions](/doc/controllers/charges.md#get-charge-transactions)
* [Update Charge Due Date](/doc/controllers/charges.md#update-charge-due-date)
* [Get Charges](/doc/controllers/charges.md#get-charges)
* [Capture Charge](/doc/controllers/charges.md#capture-charge)
* [Update Charge Card](/doc/controllers/charges.md#update-charge-card)
* [Get Charge](/doc/controllers/charges.md#get-charge)
* [Get Charges Summary](/doc/controllers/charges.md#get-charges-summary)
* [Retry Charge](/doc/controllers/charges.md#retry-charge)
* [Cancel Charge](/doc/controllers/charges.md#cancel-charge)
* [Create Charge](/doc/controllers/charges.md#create-charge)
* [Confirm Payment](/doc/controllers/charges.md#confirm-payment)


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
| `request` | [`UpdateMetadataRequest`](/doc/models/update-metadata-request.md) | Body, Required | Request for updating the charge metadata |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'
request = UpdateMetadataRequest()
request.metadata = {'key0' : 'metadata3' } 

result = charges_controller.update_charge_metadata(charge_id, request)
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
| `request` | [`UpdateChargePaymentMethodRequest`](/doc/models/update-charge-payment-method-request.md) | Body, Required | Request for updating the payment method from a charge |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'
request = UpdateChargePaymentMethodRequest()
request.update_subscription = False
request.payment_method = 'payment_method4'
request.credit_card = CreateCreditCardPaymentRequest()
request.debit_card = CreateDebitCardPaymentRequest()
request.boleto = CreateBoletoPaymentRequest()
request.boleto.retries = 10
request.boleto.bank = 'bank4'
request.boleto.instructions = 'instructions4'
request.boleto.billing_address = CreateAddressRequest()
request.boleto.billing_address.street = 'street8'
request.boleto.billing_address.number = 'number4'
request.boleto.billing_address.zip_code = 'zip_code2'
request.boleto.billing_address.neighborhood = 'neighborhood4'
request.boleto.billing_address.city = 'city2'
request.boleto.billing_address.state = 'state6'
request.boleto.billing_address.country = 'country2'
request.boleto.billing_address.complement = 'complement6'
request.boleto.billing_address.metadata = {'key0' : 'metadata5' } 
request.boleto.billing_address.line_1 = 'line_18'
request.boleto.billing_address.line_2 = 'line_26'
request.boleto.billing_address_id = 'billing_address_id2'
request.boleto.document_number = 'document_number0'
request.boleto.statement_descriptor = 'statement_descriptor6'
request.voucher = CreateVoucherPaymentRequest()
request.cash = CreateCashPaymentRequest()
request.cash.description = 'description6'
request.cash.confirm = False
request.bank_transfer = CreateBankTransferPaymentRequest()
request.bank_transfer.bank = 'bank4'
request.bank_transfer.retries = 204
request.private_label = CreatePrivateLabelPaymentRequest()

result = charges_controller.update_charge_payment_method(charge_id, request)
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

[`ListChargeTransactionsResponse`](/doc/models/list-charge-transactions-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.get_charge_transactions(charge_id)
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
| `request` | [`UpdateChargeDueDateRequest`](/doc/models/update-charge-due-date-request.md) | Body, Required | Request for updating the due date |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'
request = UpdateChargeDueDateRequest()

result = charges_controller.update_charge_due_date(charge_id, request)
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

[`ListChargesResponse`](/doc/models/list-charges-response.md)

## Example Usage

```python
result = charges_controller.get_charges()
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
| `request` | [`CreateCaptureChargeRequest`](/doc/models/create-capture-charge-request.md) | Body, Optional | Request for capturing a charge |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.capture_charge(charge_id)
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
| `request` | [`UpdateChargeCardRequest`](/doc/models/update-charge-card-request.md) | Body, Required | Request for updating a charge's card |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'
request = UpdateChargeCardRequest()
request.update_subscription = False
request.card_id = 'card_id2'
request.card = CreateCardRequest()
request.card.number = 'number2'
request.card.holder_name = 'holder_name6'
request.card.exp_month = 80
request.card.exp_year = 216
request.card.cvv = 'cvv8'
request.card.billing_address = CreateAddressRequest()
request.card.billing_address.street = 'street2'
request.card.billing_address.number = 'number0'
request.card.billing_address.zip_code = 'zip_code6'
request.card.billing_address.neighborhood = 'neighborhood8'
request.card.billing_address.city = 'city8'
request.card.billing_address.state = 'state2'
request.card.billing_address.country = 'country6'
request.card.billing_address.complement = 'complement2'
request.card.billing_address.metadata = {'key0' : 'metadata1' } 
request.card.billing_address.line_1 = 'line_14'
request.card.billing_address.line_2 = 'line_20'
request.card.brand = 'brand4'
request.card.billing_address_id = 'billing_address_id6'
request.card.metadata = {'key0' : 'metadata3', 'key1' : 'metadata4', 'key2' : 'metadata5' } 
request.card.mtype = 'credit'
request.card.options = CreateCardOptionsRequest()
request.card.options.verify_card = False
request.card.private_label = False
request.card.label = 'label0'
request.recurrence = False

result = charges_controller.update_charge_card(charge_id, request)
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

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.get_charge(charge_id)
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

[`GetChargesSummaryResponse`](/doc/models/get-charges-summary-response.md)

## Example Usage

```python
status = 'status8'

result = charges_controller.get_charges_summary(status)
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

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.retry_charge(charge_id)
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
| `request` | [`CreateCancelChargeRequest`](/doc/models/create-cancel-charge-request.md) | Body, Optional | Request for cancelling a charge |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.cancel_charge(charge_id)
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
| `request` | [`CreateChargeRequest`](/doc/models/create-charge-request.md) | Body, Required | Request for creating a charge |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
request = CreateChargeRequest()
request.code = 'code4'
request.amount = 242
request.customer_id = 'customer_id4'
request.customer = CreateCustomerRequest()
request.customer.name = '{\n    "name": "Tony Stark"\n}'
request.customer.email = 'email0'
request.customer.document = 'document0'
request.customer.mtype = 'type4'
request.customer.address = CreateAddressRequest()
request.customer.address.street = 'street2'
request.customer.address.number = 'number0'
request.customer.address.zip_code = 'zip_code6'
request.customer.address.neighborhood = 'neighborhood8'
request.customer.address.city = 'city2'
request.customer.address.state = 'state8'
request.customer.address.country = 'country6'
request.customer.address.complement = 'complement8'
request.customer.address.metadata = {'key0' : 'metadata7', 'key1' : 'metadata6' } 
request.customer.address.line_1 = 'line_16'
request.customer.address.line_2 = 'line_20'
request.customer.metadata = {'key0' : 'metadata3', 'key1' : 'metadata2', 'key2' : 'metadata1' } 
request.customer.phones = CreatePhonesRequest()
request.customer.code = 'code4'
request.payment = CreatePaymentRequest()
request.payment.payment_method = 'payment_method2'
request.payment.private_label = CreatePrivateLabelPaymentRequest()
request.metadata = {'key0' : 'metadata3' } 
request.antifraud = CreateAntifraudRequest()
request.antifraud.mtype = 'type0'
request.antifraud.clearsale = CreateClearSaleRequest()
request.antifraud.clearsale.custom_sla = 52
request.order_id = 'order_id0'

result = charges_controller.create_charge(request)
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
| `request` | [`CreateConfirmPaymentRequest`](/doc/models/create-confirm-payment-request.md) | Body, Optional | Request for confirm payment |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetChargeResponse`](/doc/models/get-charge-response.md)

## Example Usage

```python
charge_id = 'charge_id8'

result = charges_controller.confirm_payment(charge_id)
```

