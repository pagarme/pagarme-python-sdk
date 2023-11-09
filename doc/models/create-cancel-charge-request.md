
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

## Example (as JSON)

```json
{
  "amount": 244,
  "split_rules": [
    {
      "id": "id2",
      "Amount": 244,
      "type": "type8"
    }
  ],
  "split": [
    {
      "type": "type2",
      "amount": 10,
      "recipient_id": "recipient_id2",
      "options": {
        "liable": false,
        "charge_processing_fee": false,
        "charge_remainder_fee": false
      },
      "split_rule_id": "split_rule_id0"
    }
  ],
  "operation_reference": "operation_reference8",
  "bank_account": {
    "holder_name": "holder_name0",
    "holder_type": "holder_type6",
    "holder_document": "holder_document8",
    "bank": "bank2",
    "branch_number": "branch_number0",
    "branch_check_digit": "branch_check_digit0",
    "account_number": "account_number4",
    "account_check_digit": "account_check_digit0",
    "type": "type6"
  }
}
```

