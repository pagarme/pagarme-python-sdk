
# Create Transfer Request

Request for creating a transfer

## Structure

`CreateTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Transfer amount |
| `metadata` | `dict` | Required | Metadata |

## Example (as JSON)

```json
{
  "amount": 46,
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  }
}
```

