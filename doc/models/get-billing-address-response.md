
# Get Billing Address Response

Response object for getting a billing address

## Structure

`GetBillingAddressResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `string` | Required | - |
| `number` | `string` | Required | - |
| `zip_code` | `string` | Required | - |
| `neighborhood` | `string` | Required | - |
| `city` | `string` | Required | - |
| `state` | `string` | Required | - |
| `country` | `string` | Required | - |
| `complement` | `string` | Required | - |
| `line_1` | `string` | Required | Line 1 for address |
| `line_2` | `string` | Required | Line 2 for address |

## Example (as JSON)

```json
{
  "street": "street0",
  "number": "number2",
  "zip_code": "zip_code4",
  "neighborhood": "neighborhood6",
  "city": "city0",
  "state": "state4",
  "country": "country4",
  "complement": "complement4",
  "line_1": "line_16",
  "line_2": "line_28"
}
```

