
# Create Bank Account Refunding DTO

Bank Account

## Structure

`CreateBankAccountRefundingDTO`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holder_name` | `str` | Required | Nome/razão social do favorecido |
| `holder_type` | `str` | Required | Tipo de titular (pessoa física ou jurídica) |
| `holder_document` | `str` | Required | CPF ou CNPJ do favorecido |
| `bank` | `str` | Required | Dígitos que identificam cada banco. |
| `branch_number` | `str` | Required | Número da agência bancária |
| `branch_check_digit` | `str` | Required | Dígito da agência bancária |
| `account_number` | `str` | Required | Número da conta |
| `account_check_digit` | `str` | Required | Dígito verificador da conta |
| `mtype` | `str` | Required | Tipo de conta |

## Example (as JSON)

```json
{
  "holder_name": "holder_name2",
  "holder_type": "holder_type8",
  "holder_document": "holder_document0",
  "bank": "bank4",
  "branch_number": "branch_number2",
  "branch_check_digit": "branch_check_digit2",
  "account_number": "account_number6",
  "account_check_digit": "account_check_digit2",
  "type": "type4"
}
```

