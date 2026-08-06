
# Get Gateway Recipient Response

Information about the recipient on the gateway

## Structure

`GetGatewayRecipientResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gateway` | `str` | Optional | Gateway name |
| `status` | `str` | Optional | Status of the recipient on the gateway |
| `pgid` | `str` | Optional | Recipient id on the gateway |
| `created_at` | `str` | Optional | Creation date |
| `updated_at` | `str` | Optional | Last update date |

## Example

```python
from pagarmeapisdk.models.get_gateway_recipient_response import GetGatewayRecipientResponse

get_gateway_recipient_response = GetGatewayRecipientResponse(
    gateway='gateway6',
    status='status2',
    pgid='pgid8',
    created_at='created_at6',
    updated_at='updated_at8'
)
```

