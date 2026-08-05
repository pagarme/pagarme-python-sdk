# Recipients

```python
recipients_controller = client.recipients
```

## Class Name

`RecipientsController`

## Methods

* [Create Anticipation](../../doc/controllers/recipients.md#create-anticipation)
* [Create KYC Link](../../doc/controllers/recipients.md#create-kyc-link)
* [Create Recipient](../../doc/controllers/recipients.md#create-recipient)
* [Create Transfer](../../doc/controllers/recipients.md#create-transfer)
* [Create Withdraw](../../doc/controllers/recipients.md#create-withdraw)
* [Get Anticipation](../../doc/controllers/recipients.md#get-anticipation)
* [Get Anticipation Limits](../../doc/controllers/recipients.md#get-anticipation-limits)
* [Get Anticipations](../../doc/controllers/recipients.md#get-anticipations)
* [Get Balance](../../doc/controllers/recipients.md#get-balance)
* [Get Default Recipient](../../doc/controllers/recipients.md#get-default-recipient)
* [Get Recipient](../../doc/controllers/recipients.md#get-recipient)
* [Get Recipient by Code](../../doc/controllers/recipients.md#get-recipient-by-code)
* [Get Recipients](../../doc/controllers/recipients.md#get-recipients)
* [Get Transfer](../../doc/controllers/recipients.md#get-transfer)
* [Get Transfers](../../doc/controllers/recipients.md#get-transfers)
* [Get Withdraw by Id](../../doc/controllers/recipients.md#get-withdraw-by-id)
* [Get Withdrawals](../../doc/controllers/recipients.md#get-withdrawals)
* [Update Automatic Anticipation Settings](../../doc/controllers/recipients.md#update-automatic-anticipation-settings)
* [Update Recipient](../../doc/controllers/recipients.md#update-recipient)
* [Update Recipient Code](../../doc/controllers/recipients.md#update-recipient-code)
* [Update Recipient Default Bank Account](../../doc/controllers/recipients.md#update-recipient-default-bank-account)
* [Update Recipient Metadata](../../doc/controllers/recipients.md#update-recipient-metadata)
* [Update Recipient Transfer Settings](../../doc/controllers/recipients.md#update-recipient-transfer-settings)


# Create Anticipation

Creates an anticipation

```python
def create_anticipation(self,
                       recipient_id,
                       request,
                       idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`CreateAnticipationRequest`](../../doc/models/create-anticipation-request.md) | Body, Required | Anticipation data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetAnticipationResponse`](../../doc/models/get-anticipation-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = CreateAnticipationRequest(
    amount=242,
    timeframe='timeframe8',
    payment_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

result = recipients_controller.create_anticipation(
    recipient_id,
    request
)
print(result)
```


# Create KYC Link

Create a KYC link

```python
def create_kyc_link(self,
                   recipient_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |

## Response Type

**200**

[`CreateKYCLinkResponse`](../../doc/models/create-kyc-link-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.create_kyc_link(recipient_id)
print(result)
```


# Create Recipient

Creates a new recipient

```python
def create_recipient(self,
                    request,
                    idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`CreateRecipientRequest`](../../doc/models/create-recipient-request.md) | Body, Required | Recipient data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
request = CreateRecipientRequest(
    default_bank_account=CreateBankAccountRequest(
        holder_name=None,
        holder_type=None,
        holder_document=None,
        bank=None,
        branch_number=None,
        account_number=None,
        account_check_digit=None,
        mtype=None,
        metadata={}
    ),
    metadata={},
    code=None,
    payment_mode='bank_transfer'
)

result = recipients_controller.create_recipient(request)
print(result)
```


# Create Transfer

Creates a transfer for a recipient

```python
def create_transfer(self,
                   recipient_id,
                   request,
                   idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient Id |
| `request` | [`CreateTransferRequest`](../../doc/models/create-transfer-request.md) | Body, Required | Transfer data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetTransferResponse`](../../doc/models/get-transfer-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = CreateTransferRequest(
    amount=242,
    metadata={
        'key0': 'metadata3'
    }
)

result = recipients_controller.create_transfer(
    recipient_id,
    request
)
print(result)
```


# Create Withdraw

```python
def create_withdraw(self,
                   recipient_id,
                   request)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | - |
| `request` | [`CreateWithdrawRequest`](../../doc/models/create-withdraw-request.md) | Body, Required | - |

## Response Type

**200**

[`GetWithdrawResponse`](../../doc/models/get-withdraw-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = CreateWithdrawRequest(
    amount=242
)

result = recipients_controller.create_withdraw(
    recipient_id,
    request
)
print(result)
```


# Get Anticipation

Gets an anticipation

```python
def get_anticipation(self,
                    recipient_id,
                    anticipation_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `anticipation_id` | `str` | Template, Required | Anticipation id |

## Response Type

**200**

[`GetAnticipationResponse`](../../doc/models/get-anticipation-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

anticipation_id = 'anticipation_id0'

result = recipients_controller.get_anticipation(
    recipient_id,
    anticipation_id
)
print(result)
```


# Get Anticipation Limits

Gets the anticipation limits for a recipient

```python
def get_anticipation_limits(self,
                           recipient_id,
                           timeframe,
                           payment_date)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `timeframe` | `str` | Query, Required | Timeframe |
| `payment_date` | `datetime` | Query, Required | Anticipation payment date |

## Response Type

**200**

[`GetAnticipationLimitResponse`](../../doc/models/get-anticipation-limit-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

timeframe = 'timeframe2'

payment_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = recipients_controller.get_anticipation_limits(
    recipient_id,
    timeframe,
    payment_date
)
print(result)
```


# Get Anticipations

Retrieves a paginated list of anticipations from a recipient

```python
def get_anticipations(self,
                     recipient_id,
                     page=None,
                     size=None,
                     status=None,
                     timeframe=None,
                     payment_date_since=None,
                     payment_date_until=None,
                     created_since=None,
                     created_until=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `status` | `str` | Query, Optional | Filter for anticipation status |
| `timeframe` | `str` | Query, Optional | Filter for anticipation timeframe |
| `payment_date_since` | `datetime` | Query, Optional | Filter for start range for anticipation payment date |
| `payment_date_until` | `datetime` | Query, Optional | Filter for end range for anticipation payment date |
| `created_since` | `datetime` | Query, Optional | Filter for start range for anticipation creation date |
| `created_until` | `datetime` | Query, Optional | Filter for end range for anticipation creation date |

## Response Type

**200**

[`ListAnticipationResponse`](../../doc/models/list-anticipation-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_anticipations(recipient_id)
print(result)
```


# Get Balance

Get balance information for a recipient

```python
def get_balance(self,
               recipient_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |

## Response Type

**200**

[`GetBalanceResponse`](../../doc/models/get-balance-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_balance(recipient_id)
print(result)
```


# Get Default Recipient

```python
def get_default_recipient(self)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
result = recipients_controller.get_default_recipient()
print(result)
```


# Get Recipient

Retrieves recipient information

```python
def get_recipient(self,
                 recipient_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipiend id |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_recipient(recipient_id)
print(result)
```


# Get Recipient by Code

Retrieves recipient information

```python
def get_recipient_by_code(self,
                         code)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Template, Required | Recipient code |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
code = 'code8'

result = recipients_controller.get_recipient_by_code(code)
print(result)
```


# Get Recipients

Retrieves paginated recipients information

```python
def get_recipients(self,
                  page=None,
                  size=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |

## Response Type

**200**

[`ListRecipientResponse`](../../doc/models/list-recipient-response.md)

## Example Usage

```python
result = recipients_controller.get_recipients()
print(result)
```


# Get Transfer

Gets a transfer

```python
def get_transfer(self,
                recipient_id,
                transfer_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `transfer_id` | `str` | Template, Required | Transfer id |

## Response Type

**200**

[`GetTransferResponse`](../../doc/models/get-transfer-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

transfer_id = 'transfer_id6'

result = recipients_controller.get_transfer(
    recipient_id,
    transfer_id
)
print(result)
```


# Get Transfers

Gets a paginated list of transfers for the recipient

```python
def get_transfers(self,
                 recipient_id,
                 page=None,
                 size=None,
                 status=None,
                 created_since=None,
                 created_until=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `status` | `str` | Query, Optional | Filter for transfer status |
| `created_since` | `datetime` | Query, Optional | Filter for start range of transfer creation date |
| `created_until` | `datetime` | Query, Optional | Filter for end range of transfer creation date |

## Response Type

**200**

[`ListTransferResponse`](../../doc/models/list-transfer-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_transfers(recipient_id)
print(result)
```


# Get Withdraw by Id

```python
def get_withdraw_by_id(self,
                      recipient_id,
                      withdrawal_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | - |
| `withdrawal_id` | `str` | Template, Required | - |

## Response Type

**200**

[`GetWithdrawResponse`](../../doc/models/get-withdraw-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

withdrawal_id = 'withdrawal_id2'

result = recipients_controller.get_withdraw_by_id(
    recipient_id,
    withdrawal_id
)
print(result)
```


# Get Withdrawals

Gets a paginated list of transfers for the recipient

```python
def get_withdrawals(self,
                   recipient_id,
                   page=None,
                   size=None,
                   status=None,
                   created_since=None,
                   created_until=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | - |
| `page` | `int` | Query, Optional | - |
| `size` | `int` | Query, Optional | - |
| `status` | `str` | Query, Optional | - |
| `created_since` | `datetime` | Query, Optional | - |
| `created_until` | `datetime` | Query, Optional | - |

## Response Type

**200**

[`ListWithdrawals`](../../doc/models/list-withdrawals.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_withdrawals(recipient_id)
print(result)
```


# Update Automatic Anticipation Settings

Updates recipient metadata

```python
def update_automatic_anticipation_settings(self,
                                          recipient_id,
                                          request,
                                          idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateAutomaticAnticipationSettingsRequest`](../../doc/models/update-automatic-anticipation-settings-request.md) | Body, Required | Metadata |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = UpdateAutomaticAnticipationSettingsRequest()

result = recipients_controller.update_automatic_anticipation_settings(
    recipient_id,
    request
)
print(result)
```


# Update Recipient

Updates a recipient

```python
def update_recipient(self,
                    recipient_id,
                    request,
                    idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateRecipientRequest`](../../doc/models/update-recipient-request.md) | Body, Required | Recipient data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = UpdateRecipientRequest(
    name='name6',
    email='email0',
    description='description6',
    mtype='type4',
    status='status8',
    metadata={
        'key0': 'metadata3'
    }
)

result = recipients_controller.update_recipient(
    recipient_id,
    request
)
print(result)
```


# Update Recipient Code

Updates recipient code

```python
def update_recipient_code(self,
                         recipient_id,
                         request,
                         idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateRecipientCodeRequest`](../../doc/models/update-recipient-code-request.md) | Body, Required | UpdateRecipientCodeRequest |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = UpdateRecipientCodeRequest(
    code='code4'
)

result = recipients_controller.update_recipient_code(
    recipient_id,
    request
)
print(result)
```


# Update Recipient Default Bank Account

Updates the default bank account from a recipient

```python
def update_recipient_default_bank_account(self,
                                         recipient_id,
                                         request,
                                         idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateRecipientBankAccountRequest`](../../doc/models/update-recipient-bank-account-request.md) | Body, Required | Bank account data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = UpdateRecipientBankAccountRequest(
    bank_account=CreateBankAccountRequest(
        holder_name=None,
        holder_type=None,
        holder_document=None,
        bank=None,
        branch_number=None,
        account_number=None,
        account_check_digit=None,
        mtype=None,
        metadata={}
    ),
    payment_mode='bank_transfer'
)

result = recipients_controller.update_recipient_default_bank_account(
    recipient_id,
    request
)
print(result)
```


# Update Recipient Metadata

Updates recipient metadata

```python
def update_recipient_metadata(self,
                             recipient_id,
                             request,
                             idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Metadata |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = UpdateMetadataRequest(
    metadata={
        'key0': 'metadata3'
    }
)

result = recipients_controller.update_recipient_metadata(
    recipient_id,
    request
)
print(result)
```


# Update Recipient Transfer Settings

```python
def update_recipient_transfer_settings(self,
                                      recipient_id,
                                      request,
                                      idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient Identificator |
| `request` | [`UpdateTransferSettingsRequest`](../../doc/models/update-transfer-settings-request.md) | Body, Required | - |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = UpdateTransferSettingsRequest(
    transfer_enabled='transfer_enabled2',
    transfer_interval='transfer_interval6',
    transfer_day='transfer_day6'
)

result = recipients_controller.update_recipient_transfer_settings(
    recipient_id,
    request
)
print(result)
```

