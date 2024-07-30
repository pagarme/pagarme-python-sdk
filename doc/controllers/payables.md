# Payables

```python
payables_controller = client.payables
```

## Class Name

`PayablesController`

## Methods

* [Get Payables](../../doc/controllers/payables.md#get-payables)
* [Get Payable by Id](../../doc/controllers/payables.md#get-payable-by-id)


# Get Payables

```python
def get_payables(self,
                mtype=None,
                split_id=None,
                bulk_anticipation_id=None,
                installment=None,
                status=None,
                recipient_id=None,
                amount=None,
                charge_id=None,
                payment_date_until=None,
                payment_date_since=None,
                updated_until=None,
                updated_since=None,
                created_until=None,
                created_since=None,
                liquidation_arrangement_id=None,
                page=None,
                size=None,
                gateway_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Query, Optional | - |
| `split_id` | `str` | Query, Optional | - |
| `bulk_anticipation_id` | `str` | Query, Optional | - |
| `installment` | `int` | Query, Optional | - |
| `status` | `str` | Query, Optional | - |
| `recipient_id` | `str` | Query, Optional | - |
| `amount` | `int` | Query, Optional | - |
| `charge_id` | `str` | Query, Optional | - |
| `payment_date_until` | `str` | Query, Optional | - |
| `payment_date_since` | `datetime` | Query, Optional | - |
| `updated_until` | `datetime` | Query, Optional | - |
| `updated_since` | `datetime` | Query, Optional | - |
| `created_until` | `datetime` | Query, Optional | - |
| `created_since` | `datetime` | Query, Optional | - |
| `liquidation_arrangement_id` | `str` | Query, Optional | - |
| `page` | `int` | Query, Optional | - |
| `size` | `int` | Query, Optional | - |
| `gateway_id` | `long\|int` | Query, Optional | - |

## Response Type

[`ListPayablesResponse`](../../doc/models/list-payables-response.md)

## Example Usage

```python
result = payables_controller.get_payables()
```


# Get Payable by Id

```python
def get_payable_by_id(self,
                     id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Template, Required | - |

## Response Type

[`GetPayableResponse`](../../doc/models/get-payable-response.md)

## Example Usage

```python
id = 112

result = payables_controller.get_payable_by_id(id)
```

