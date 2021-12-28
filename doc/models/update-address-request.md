
# Update Address Request

Request for updating an address

## Structure

`UpdateAddressRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `string` | Required | Number |
| `complement` | `string` | Required | Complement |
| `metadata` | `dict` | Required | Metadata |
| `line_2` | `string` | Required | Line 2 for address |

## Example (as JSON)

```json
{
  "number": "number2",
  "complement": "complement4",
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  },
  "line_2": "line_28"
}
```

