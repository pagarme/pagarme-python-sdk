
# Update Recipient Bank Account Request

Updates the default bank account for a recipient

## Structure

`UpdateRecipientBankAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account` | [`CreateBankAccountRequest`](../../doc/models/create-bank-account-request.md) | Required | Bank account |
| `payment_mode` | `string` | Required | Payment mode<br>**Default**: `'bank_transfer'` |

## Example (as JSON)

```json
{
  "bank_account": null,
  "payment_mode": "bank_transfer"
}
```

