
# Create Three D Secure Request

Creates a 3D-S authentication payment

## Structure

`CreateThreeDSecureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mpi` | `str` | Required | The MPI Vendor (MerchantPlugin) |
| `cavv` | `str` | Optional | The Cardholder Authentication Verification value |
| `eci` | `str` | Optional | The Electronic Commerce Indicator value |
| `transaction_id` | `str` | Optional | The TransactionId value (XID) |
| `success_url` | `str` | Optional | The success URL after the authentication |
| `ds_transaction_id` | `str` | Optional | Directory Service Transaction Identifier |
| `version` | `str` | Optional | ThreeDSecure Version |

## Example (as JSON)

```json
{
  "mpi": "mpi4",
  "cavv": "cavv2",
  "eci": "eci6",
  "transaction_id": "transaction_id4",
  "success_url": "success_url8",
  "ds_transaction_id": "ds_transaction_id4"
}
```

