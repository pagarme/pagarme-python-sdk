# Transfers

```python
transfers_controller = client.transfers
```

## Class Name

`TransfersController`

## Methods

* [Get Transfer by Id](/doc/controllers/transfers.md#get-transfer-by-id)
* [Create Transfer](/doc/controllers/transfers.md#create-transfer)
* [Get Transfers](/doc/controllers/transfers.md#get-transfers)


# Get Transfer by Id

```python
def get_transfer_by_id(self,
                      transfer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_id` | `string` | Template, Required | - |

## Response Type

[`GetTransfer`](/doc/models/get-transfer.md)

## Example Usage

```python
transfer_id = 'transfer_id6'

result = transfers_controller.get_transfer_by_id(transfer_id)
```


# Create Transfer

```python
def create_transfer(self,
                   request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`CreateTransfer`](/doc/models/create-transfer.md) | Body, Required | - |

## Response Type

[`GetTransfer`](/doc/models/get-transfer.md)

## Example Usage

```python
request = CreateTransfer()
request.amount = 242
request.source_id = 'source_id0'
request.target_id = 'target_id6'

result = transfers_controller.create_transfer(request)
```


# Get Transfers

Gets all transfers

```python
def get_transfers(self)
```

## Response Type

[`ListTransfers`](/doc/models/list-transfers.md)

## Example Usage

```python
result = transfers_controller.get_transfers()
```

