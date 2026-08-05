
# Create Capture Charge Request

Request for capturing a charge

## Structure

`CreateCaptureChargeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Required | Code for the charge. Sending this field will update the code send on the charge and order creation. |
| `amount` | `int` | Optional | The amount that will be captured |
| `split` | [`List[CreateSplitRequest]`](../../doc/models/create-split-request.md) | Optional | Splits |
| `operation_reference` | `str` | Required | - |

## Example

```python
from pagarmeapisdk.models.create_capture_charge_request import CreateCaptureChargeRequest

create_capture_charge_request = CreateCaptureChargeRequest(
    code='code8',
    operation_reference='operation_reference0',
    amount=34,
    split=[
        None
    ]
)
```

