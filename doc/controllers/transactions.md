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

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `string` | Template, Required | - |

## Response Type

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Example Usage

```python
transaction_id = 'transaction_id8'

result = transactions_controller.get_transaction(transaction_id)
```

