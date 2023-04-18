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
| `public_key` | `string` | Template, Required | Public key |
| `request` | [`CreateTokenRequest`](../../doc/models/create-token-request.md) | Body, Required | Request for creating a token |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetTokenResponse`](../../doc/models/get-token-response.md)

## Example Usage

```python
public_key = 'public_key6'

request = CreateTokenRequest(
    mtype='card',
    card=CreateCardTokenRequest(
        number='number2',
        holder_name='holder_name6',
        exp_month=80,
        exp_year=216,
        cvv='cvv8',
        brand='brand4',
        label='label0'
    )
)

result = tokens_controller.create_token(
    public_key,
    request
)
print(result)
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
| `id` | `string` | Template, Required | Token id |
| `public_key` | `string` | Template, Required | Public key |

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
print(result)
```

