# Balance Operations

```python
balance_operations_controller = client.balance_operations
```

## Class Name

`BalanceOperationsController`

## Methods

* [Get Balance Operations](../../doc/controllers/balance-operations.md#get-balance-operations)
* [Get Balance Operation by Id](../../doc/controllers/balance-operations.md#get-balance-operation-by-id)


# Get Balance Operations

```python
def get_balance_operations(self,
                          status=None,
                          created_since=None,
                          created_until=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Query, Optional | - |
| `created_since` | `datetime` | Query, Optional | - |
| `created_until` | `datetime` | Query, Optional | - |

## Response Type

[`ListBalanceOperationResponse`](../../doc/models/list-balance-operation-response.md)

## Example Usage

```python
result = balance_operations_controller.get_balance_operations()
print(result)
```


# Get Balance Operation by Id

```python
def get_balance_operation_by_id(self,
                               id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | - |

## Response Type

[`GetBalanceOperationResponse`](../../doc/models/get-balance-operation-response.md)

## Example Usage

```python
id = 112

result = balance_operations_controller.get_balance_operation_by_id(id)
print(result)
```

