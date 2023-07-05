
# Create Bank Account Refunding DTO

Bank Account

## Structure

`CreateBankAccountRefundingDTO`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holder_name` | `string` | Required | Nome/razão social do favorecido |
| `holder_type` | `string` | Required | Tipo de titular (pessoa física ou jurídica) |
| `holder_document` | `string` | Required | CPF ou CNPJ do favorecido |
| `bank` | `string` | Required | Dígitos que identificam cada banco. |
| `branch_number` | `string` | Required | Número da agência bancária |
| `branch_check_digit` | `string` | Required | Dígito da agência bancária |
| `account_number` | `string` | Required | Número da conta |
| `account_check_digit` | `string` | Required | Dígito verificador da conta |
| `mtype` | `string` | Required | Tipo de conta |

## Example (as JSON)

```json
{
  "holder_name": "holder_name4",
  "holder_type": "holder_type2",
  "holder_document": "holder_document6",
  "bank": "bank8",
  "branch_number": "branch_number6",
  "branch_check_digit": "branch_check_digit4",
  "account_number": "account_number0",
  "account_check_digit": "account_check_digit6",
  "type": "type0"
}
```

