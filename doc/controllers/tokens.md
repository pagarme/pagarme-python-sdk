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

**200**

[`GetTokenResponse`](../../doc/models/get-token-response.md)

## Example Usage

```python
public_key = 'public_key6'

request = CreateTokenRequest(
    mtype='card',
    card=CreateCardTokenRequest(
        number=None,
        holder_name=None,
        exp_month=None,
        exp_year=None,
        cvv=None,
        brand=None,
        label=None
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
| `id` | `str` | Template, Required | Token id |
| `public_key` | `str` | Template, Required | Public key |

## Response Type

**200**

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

