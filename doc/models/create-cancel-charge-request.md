
# Create Cancel Charge Request

Request for canceling a charge.

## Structure

`CreateCancelChargeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | The amount that will be canceled. |
| `split_rules` | [`List[CreateCancelChargeSplitRulesRequest]`](../../doc/models/create-cancel-charge-split-rules-request.md) | Optional | The split rules request |
| `split` | [`List[CreateSplitRequest]`](../../doc/models/create-split-request.md) | Optional | Splits |
| `operation_reference` | `str` | Required | - |
| `bank_account` | [`CreateBankAccountRefundingDTO`](../../doc/models/create-bank-account-refunding-dto.md) | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_bank_account_refunding_dto import CreateBankAccountRefundingDTO
from pagarmeapisdk.models.create_cancel_charge_request import CreateCancelChargeRequest

create_cancel_charge_request = CreateCancelChargeRequest(
    operation_reference='operation_reference0',
    amount=4,
    split_rules=[
        None
    ],
    split=[
        None
    ],
    bank_account=CreateBankAccountRefundingDTO(
        holder_name=None,
        holder_type=None,
        holder_document=None,
        bank=None,
        branch_number=None,
        branch_check_digit=None,
        account_number=None,
        account_check_digit=None,
        mtype=None
    )
)
```

