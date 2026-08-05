
# Create Emv Data Tlv Decrypt Request

## Structure

`CreateEmvDataTlvDecryptRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tag` | `str` | Required | Emv tag |
| `lenght` | `str` | Required | Emv lenght |
| `value` | `str` | Required | Emv value |

## Example

```python
from pagarmeapisdk.models.create_emv_data_tlv_decrypt_request import CreateEmvDataTlvDecryptRequest

create_emv_data_tlv_decrypt_request = CreateEmvDataTlvDecryptRequest(
    tag='tag6',
    lenght='lenght6',
    value='value4'
)
```

