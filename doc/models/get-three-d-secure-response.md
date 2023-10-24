
# Get Three D Secure Response

3D-S payment authentication response

## Structure

`GetThreeDSecureResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mpi` | `str` | Optional | MPI Vendor |
| `eci` | `str` | Optional | Electronic Commerce Indicator (ECI) (Opcional) |
| `cavv` | `str` | Optional | Online payment cryptogram, definido pelo 3-D Secure. |
| `transaction_id` | `str` | Optional | Identificador da transação (XID) |
| `success_url` | `str` | Optional | Url de redirecionamento de sucessso |

## Example (as JSON)

```json
{
  "mpi": "mpi2",
  "eci": "eci4",
  "cavv": "cavv0",
  "transaction_Id": "transaction_Id0",
  "success_url": "success_url6"
}
```

