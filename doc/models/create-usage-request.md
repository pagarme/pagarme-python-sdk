
# Create Usage Request

Request for creating a usage

## Structure

`CreateUsageRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quantity` | `int` | Required | - |
| `description` | `string` | Required | - |
| `used_at` | `datetime` | Required | - |
| `code` | `string` | Optional | Identification code in the client system |
| `group` | `string` | Optional | identification group in the client system |
| `amount` | `int` | Optional | Field used in item scheme type 'Percent' |

## Example (as JSON)

```json
{
  "quantity": 68,
  "description": "description0",
  "used_at": "2016-03-13T12:52:32.123Z",
  "code": null,
  "group": null,
  "amount": null
}
```

