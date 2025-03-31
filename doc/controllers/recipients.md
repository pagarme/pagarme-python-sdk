# Recipients

```python
recipients_controller = client.recipients
```

## Class Name

`RecipientsController`

## Methods

* [Update Recipient](../../doc/controllers/recipients.md#update-recipient)
* [Create Anticipation](../../doc/controllers/recipients.md#create-anticipation)
* [Get Anticipation Limits](../../doc/controllers/recipients.md#get-anticipation-limits)
* [Get Recipients](../../doc/controllers/recipients.md#get-recipients)
* [Get Withdraw by Id](../../doc/controllers/recipients.md#get-withdraw-by-id)
* [Update Recipient Default Bank Account](../../doc/controllers/recipients.md#update-recipient-default-bank-account)
* [Update Recipient Metadata](../../doc/controllers/recipients.md#update-recipient-metadata)
* [Get Transfers](../../doc/controllers/recipients.md#get-transfers)
* [Get Transfer](../../doc/controllers/recipients.md#get-transfer)
* [Create Withdraw](../../doc/controllers/recipients.md#create-withdraw)
* [Update Automatic Anticipation Settings](../../doc/controllers/recipients.md#update-automatic-anticipation-settings)
* [Get Anticipation](../../doc/controllers/recipients.md#get-anticipation)
* [Update Recipient Transfer Settings](../../doc/controllers/recipients.md#update-recipient-transfer-settings)
* [Get Anticipations](../../doc/controllers/recipients.md#get-anticipations)
* [Get Recipient](../../doc/controllers/recipients.md#get-recipient)
* [Get Balance](../../doc/controllers/recipients.md#get-balance)
* [Get Withdrawals](../../doc/controllers/recipients.md#get-withdrawals)
* [Create Transfer](../../doc/controllers/recipients.md#create-transfer)
* [Create Recipient](../../doc/controllers/recipients.md#create-recipient)
* [Get Recipient by Code](../../doc/controllers/recipients.md#get-recipient-by-code)
* [Get Default Recipient](../../doc/controllers/recipients.md#get-default-recipient)
* [Create KYC Link](../../doc/controllers/recipients.md#create-kyc-link)
* [Update Recipient Code](../../doc/controllers/recipients.md#update-recipient-code)


# Update Recipient

Updates a recipient

```python
def update_recipient(self,
                    recipient_id,
                    request,
                    idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateRecipientRequest`](../../doc/models/update-recipient-request.md) | Body, Required | Recipient data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

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
```


# Create Anticipation

Creates an anticipation

```python
def create_anticipation(self,
                       recipient_id,
                       request,
                       idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`CreateAnticipationRequest`](../../doc/models/create-anticipation-request.md) | Body, Required | Anticipation data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

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
```


# Get Anticipation Limits

Gets the anticipation limits for a recipient

```python
def get_anticipation_limits(self,
                           recipient_id,
                           timeframe,
                           payment_date)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `timeframe` | `str` | Query, Required | Timeframe |
| `payment_date` | `datetime` | Query, Required | Anticipation payment date |

## Response Type

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
```


# Get Recipients

Retrieves paginated recipients information

```python
def get_recipients(self,
                  page=None,
                  size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |

## Response Type

[`ListRecipientResponse`](../../doc/models/list-recipient-response.md)

## Example Usage

```python
result = recipients_controller.get_recipients()
```


# Get Withdraw by Id

```python
def get_withdraw_by_id(self,
                      recipient_id,
                      withdrawal_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | - |
| `withdrawal_id` | `str` | Template, Required | - |

## Response Type

[`GetWithdrawResponse`](../../doc/models/get-withdraw-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

withdrawal_id = 'withdrawal_id2'

result = recipients_controller.get_withdraw_by_id(
    recipient_id,
    withdrawal_id
)
```


# Update Recipient Default Bank Account

Updates the default bank account from a recipient

```python
def update_recipient_default_bank_account(self,
                                         recipient_id,
                                         request,
                                         idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateRecipientBankAccountRequest`](../../doc/models/update-recipient-bank-account-request.md) | Body, Required | Bank account data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = UpdateRecipientBankAccountRequest(
    bank_account=CreateBankAccountRequest(
        holder_name='holder_name0',
        holder_type='holder_type6',
        holder_document='holder_document8',
        bank='bank2',
        branch_number='branch_number0',
        account_number='account_number4',
        account_check_digit='account_check_digit0',
        mtype='type6',
        metadata={
            'key0': 'metadata1',
            'key1': 'metadata0'
        }
    ),
    payment_mode='bank_transfer'
)

result = recipients_controller.update_recipient_default_bank_account(
    recipient_id,
    request
)
```


# Update Recipient Metadata

Updates recipient metadata

```python
def update_recipient_metadata(self,
                             recipient_id,
                             request,
                             idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Metadata |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

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

[`ListTransferResponse`](../../doc/models/list-transfer-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_transfers(recipient_id)
```


# Get Transfer

Gets a transfer

```python
def get_transfer(self,
                recipient_id,
                transfer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `transfer_id` | `str` | Template, Required | Transfer id |

## Response Type

[`GetTransferResponse`](../../doc/models/get-transfer-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

transfer_id = 'transfer_id6'

result = recipients_controller.get_transfer(
    recipient_id,
    transfer_id
)
```


# Create Withdraw

```python
def create_withdraw(self,
                   recipient_id,
                   request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | - |
| `request` | [`CreateWithdrawRequest`](../../doc/models/create-withdraw-request.md) | Body, Required | - |

## Response Type

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
```


# Update Automatic Anticipation Settings

Updates recipient metadata

```python
def update_automatic_anticipation_settings(self,
                                          recipient_id,
                                          request,
                                          idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateAutomaticAnticipationSettingsRequest`](../../doc/models/update-automatic-anticipation-settings-request.md) | Body, Required | Metadata |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

request = UpdateAutomaticAnticipationSettingsRequest()

result = recipients_controller.update_automatic_anticipation_settings(
    recipient_id,
    request
)
```


# Get Anticipation

Gets an anticipation

```python
def get_anticipation(self,
                    recipient_id,
                    anticipation_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `anticipation_id` | `str` | Template, Required | Anticipation id |

## Response Type

[`GetAnticipationResponse`](../../doc/models/get-anticipation-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

anticipation_id = 'anticipation_id0'

result = recipients_controller.get_anticipation(
    recipient_id,
    anticipation_id
)
```


# Update Recipient Transfer Settings

```python
def update_recipient_transfer_settings(self,
                                      recipient_id,
                                      request,
                                      idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient Identificator |
| `request` | [`UpdateTransferSettingsRequest`](../../doc/models/update-transfer-settings-request.md) | Body, Required | - |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

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

[`ListAnticipationResponse`](../../doc/models/list-anticipation-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_anticipations(recipient_id)
```


# Get Recipient

Retrieves recipient information

```python
def get_recipient(self,
                 recipient_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipiend id |

## Response Type

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_recipient(recipient_id)
```


# Get Balance

Get balance information for a recipient

```python
def get_balance(self,
               recipient_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |

## Response Type

[`GetBalanceResponse`](../../doc/models/get-balance-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_balance(recipient_id)
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

[`ListWithdrawals`](../../doc/models/list-withdrawals.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.get_withdrawals(recipient_id)
```


# Create Transfer

Creates a transfer for a recipient

```python
def create_transfer(self,
                   recipient_id,
                   request,
                   idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient Id |
| `request` | [`CreateTransferRequest`](../../doc/models/create-transfer-request.md) | Body, Required | Transfer data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

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
```


# Create Recipient

Creates a new recipient

```python
def create_recipient(self,
                    request,
                    idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`CreateRecipientRequest`](../../doc/models/create-recipient-request.md) | Body, Required | Recipient data |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
request = CreateRecipientRequest(
    default_bank_account=CreateBankAccountRequest(
        holder_name='holder_name4',
        holder_type='holder_type0',
        holder_document='holder_document2',
        bank='bank6',
        branch_number='branch_number4',
        account_number='account_number8',
        account_check_digit='account_check_digit4',
        mtype='type2',
        metadata={
            'key0': 'metadata5',
            'key1': 'metadata4',
            'key2': 'metadata3'
        }
    ),
    metadata={
        'key0': 'metadata3'
    },
    code='code4',
    payment_mode='bank_transfer'
)

result = recipients_controller.create_recipient(request)
```


# Get Recipient by Code

Retrieves recipient information

```python
def get_recipient_by_code(self,
                         code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Template, Required | Recipient code |

## Response Type

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
code = 'code8'

result = recipients_controller.get_recipient_by_code(code)
```


# Get Default Recipient

```python
def get_default_recipient(self)
```

## Response Type

[`GetRecipientResponse`](../../doc/models/get-recipient-response.md)

## Example Usage

```python
result = recipients_controller.get_default_recipient()
```


# Create KYC Link

Create a KYC link

```python
def create_kyc_link(self,
                   recipient_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |

## Response Type

[`CreateKYCLinkResponse`](../../doc/models/create-kyc-link-response.md)

## Example Usage

```python
recipient_id = 'recipient_id0'

result = recipients_controller.create_kyc_link(recipient_id)
```


# Update Recipient Code

Updates recipient code

```python
def update_recipient_code(self,
                         recipient_id,
                         request,
                         idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Template, Required | Recipient id |
| `request` | [`UpdateRecipientCodeRequest`](../../doc/models/update-recipient-code-request.md) | Body, Required | UpdateRecipientCodeRequest |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

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
```

