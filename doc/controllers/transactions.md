# Transactions

```python
transactions_controller = client.transactions
```

## Class Name

`TransactionsController`


# Get Transaction

```python
def get_transaction(self,
                   transaction_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Template, Required | - |

## Response Type

**200**

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Example Usage

```python
transaction_id = 'transaction_id8'

result = transactions_controller.get_transaction(transaction_id)
print(result)
```

