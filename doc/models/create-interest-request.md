
# Create Interest Request

Interest Request

## Structure

`CreateInterestRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `days` | `int` | Required | Days |
| `mtype` | `string` | Required | Type |
| `amount` | `int` | Required | Amount |

## Example (as JSON)

```json
{
  "days": 120,
  "type": "\"percentage\" or \"flat\"",
  "amount": 46
}
```

