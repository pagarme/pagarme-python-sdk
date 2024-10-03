# Tokens

```python
tokens_controller = client.tokens
```

## Class Name

`TokensController`

## Methods

* [Create Token](../../doc/controllers/tokens.md#create-token)
* [Get Token](../../doc/controllers/tokens.md#get-token)


# Create Token

:information_source: **Note** This endpoint does not require authentication.

```python
def create_token(self,
                public_key,
                request,
                idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_key` | `str` | Template, Required | Public key |
| `request` | [`CreateTokenRequest`](../../doc/models/create-token-request.md) | Body, Required | Request for creating a token |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetTokenResponse`](../../doc/models/get-token-response.md)

## Example Usage

```python
public_key = 'public_key6'

request = CreateTokenRequest(
    mtype='card',
    card=CreateCardTokenRequest(
        number='number6',
        holder_name='holder_name2',
        exp_month=228,
        exp_year=68,
        cvv='cvv4',
        brand='brand0',
        label='label6'
    )
)

result = tokens_controller.create_token(
    public_key,
    request
)
```


# Get Token

Gets a token from its id

:information_source: **Note** This endpoint does not require authentication.

```python
def get_token(self,
             id,
             public_key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | Token id |
| `public_key` | `str` | Template, Required | Public key |

## Response Type

[`GetTokenResponse`](../../doc/models/get-token-response.md)

## Example Usage

```python
id = 'id0'

public_key = 'public_key6'

result = tokens_controller.get_token(
    id,
    public_key
)
```

