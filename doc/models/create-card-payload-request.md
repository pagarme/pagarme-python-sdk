
# Create Card Payload Request

## Structure

`CreateCardPayloadRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `google_pay` | [`CreateGooglePayRequest`](../../doc/models/create-google-pay-request.md) | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_card_payload_request import CreateCardPayloadRequest

create_card_payload_request = CreateCardPayloadRequest(
    mtype='type6',
    google_pay=None
)
```

