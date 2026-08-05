
# Create Transfer Settings Request

Informações de transferência do recebedor

## Structure

`CreateTransferSettingsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_enabled` | `bool` | Required | - |
| `transfer_interval` | `str` | Required | - |
| `transfer_day` | `int` | Required | - |

## Example

```python
from pagarmeapisdk.models.create_transfer_settings_request import CreateTransferSettingsRequest

create_transfer_settings_request = CreateTransferSettingsRequest(
    transfer_enabled=False,
    transfer_interval='transfer_interval2',
    transfer_day=114
)
```

