
# Create Interest Request

Interest Request

## Structure

`CreateInterestRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `days` | `int` | Required | Days |
| `mtype` | `str` | Required | Type |
| `amount` | `int` | Required | Amount |

## Example (as JSON)

```json
{
  "days": 4,
  "type": "\"percentage\" or \"flat\"",
  "amount": 78
}
```

