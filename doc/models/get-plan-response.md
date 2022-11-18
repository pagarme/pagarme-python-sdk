
# Get Plan Response

Response object for getting a plan

## Structure

`GetPlanResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | - |
| `name` | `string` | Required | - |
| `description` | `string` | Required | - |
| `url` | `string` | Required | - |
| `statement_descriptor` | `string` | Required | - |
| `interval` | `string` | Required | - |
| `interval_count` | `int` | Required | - |
| `billing_type` | `string` | Required | - |
| `payment_methods` | `List of string` | Required | - |
| `installments` | `List of int` | Required | - |
| `status` | `string` | Required | - |
| `currency` | `string` | Required | - |
| `created_at` | `datetime` | Required | - |
| `updated_at` | `datetime` | Required | - |
| `items` | [`List of GetPlanItemResponse`](../../doc/models/get-plan-item-response.md) | Required | - |
| `billing_days` | `List of int` | Required | - |
| `shippable` | `bool` | Required | - |
| `metadata` | `dict` | Required | - |
| `trial_period_days` | `int` | Optional | - |
| `minimum_price` | `int` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "description": "description0",
  "url": "url4",
  "statement_descriptor": "statement_descriptor0",
  "interval": "interval2",
  "interval_count": 82,
  "billing_type": "billing_type6",
  "payment_methods": [
    "payment_methods5",
    "payment_methods6"
  ],
  "installments": [
    119,
    120,
    121
  ],
  "status": "status8",
  "currency": "currency0",
  "created_at": "2016-03-13T12:52:32.123Z",
  "updated_at": "2016-03-13T12:52:32.123Z",
  "items": [
    {
      "id": "id7",
      "name": "name7",
      "status": "status1",
      "created_at": "2016-03-13T12:52:32.123Z",
      "updated_at": "2016-03-13T12:52:32.123Z",
      "pricing_scheme": {
        "price": 149,
        "scheme_type": "scheme_type1",
        "price_brackets": [
          {
            "start_quantity": 60,
            "price": 2,
            "end_quantity": null,
            "overage_price": null
          },
          {
            "start_quantity": 61,
            "price": 1,
            "end_quantity": null,
            "overage_price": null
          },
          {
            "start_quantity": 62,
            "price": 0,
            "end_quantity": null,
            "overage_price": null
          }
        ],
        "minimum_price": null,
        "percentage": null
      },
      "description": "description7",
      "plan": {
        "id": "id7",
        "name": "name7",
        "description": "description3",
        "url": "url1",
        "statement_descriptor": "statement_descriptor7",
        "interval": "interval5",
        "interval_count": 89,
        "billing_type": "billing_type9",
        "payment_methods": [
          "payment_methods8",
          "payment_methods9"
        ],
        "installments": [
          126,
          127,
          128
        ],
        "status": "status1",
        "currency": "currency7",
        "created_at": "2016-03-13T12:52:32.123Z",
        "updated_at": "2016-03-13T12:52:32.123Z",
        "items": [
          {
            "id": "id4",
            "name": "name4",
            "status": "status6",
            "created_at": "2016-03-13T12:52:32.123Z",
            "updated_at": "2016-03-13T12:52:32.123Z",
            "pricing_scheme": {
              "price": 156,
              "scheme_type": "scheme_type4",
              "price_brackets": [
                {
                  "start_quantity": 53,
                  "price": 9,
                  "end_quantity": null,
                  "overage_price": null
                },
                {
                  "start_quantity": 54,
                  "price": 8,
                  "end_quantity": null,
                  "overage_price": null
                },
                {
                  "start_quantity": 55,
                  "price": 7,
                  "end_quantity": null,
                  "overage_price": null
                }
              ],
              "minimum_price": null,
              "percentage": null
            },
            "description": "description4",
            "plan": {
              "id": "id0",
              "name": "name0",
              "description": "description0",
              "url": "url4",
              "statement_descriptor": "statement_descriptor0",
              "interval": "interval2",
              "interval_count": 82,
              "billing_type": "billing_type6",
              "payment_methods": [
                "payment_methods5",
                "payment_methods6"
              ],
              "installments": [
                119,
                120,
                121
              ],
              "status": "status8",
              "currency": "currency0",
              "created_at": "2016-03-13T12:52:32.123Z",
              "updated_at": "2016-03-13T12:52:32.123Z",
              "items": [],
              "billing_days": [
                143,
                144,
                145
              ],
              "shippable": false,
              "metadata": {
                "key0": "metadata3",
                "key1": "metadata4",
                "key2": "metadata5"
              },
              "trial_period_days": null,
              "minimum_price": null,
              "deleted_at": null
            },
            "quantity": null,
            "cycles": null,
            "deleted_at": null
          },
          {
            "id": "id5",
            "name": "name5",
            "status": "status7",
            "created_at": "2016-03-13T12:52:32.123Z",
            "updated_at": "2016-03-13T12:52:32.123Z",
            "pricing_scheme": {
              "price": 157,
              "scheme_type": "scheme_type3",
              "price_brackets": [
                {
                  "start_quantity": 52,
                  "price": 10,
                  "end_quantity": null,
                  "overage_price": null
                },
                {
                  "start_quantity": 53,
                  "price": 9,
                  "end_quantity": null,
                  "overage_price": null
                }
              ],
              "minimum_price": null,
              "percentage": null
            },
            "description": "description5",
            "plan": {
              "id": "id1",
              "name": "name1",
              "description": "description9",
              "url": "url5",
              "statement_descriptor": "statement_descriptor1",
              "interval": "interval1",
              "interval_count": 83,
              "billing_type": "billing_type5",
              "payment_methods": [
                "payment_methods4"
              ],
              "installments": [
                120
              ],
              "status": "status7",
              "currency": "currency9",
              "created_at": "2016-03-13T12:52:32.123Z",
              "updated_at": "2016-03-13T12:52:32.123Z",
              "items": [],
              "billing_days": [
                142,
                143
              ],
              "shippable": true,
              "metadata": {
                "key0": "metadata2",
                "key1": "metadata3"
              },
              "trial_period_days": null,
              "minimum_price": null,
              "deleted_at": null
            },
            "quantity": null,
            "cycles": null,
            "deleted_at": null
          }
        ],
        "billing_days": [
          120,
          119,
          118
        ],
        "shippable": true,
        "metadata": {
          "key0": "metadata6",
          "key1": "metadata7",
          "key2": "metadata8"
        },
        "trial_period_days": null,
        "minimum_price": null,
        "deleted_at": null
      },
      "quantity": null,
      "cycles": null,
      "deleted_at": null
    },
    {
      "id": "id8",
      "name": "name8",
      "status": "status0",
      "created_at": "2016-03-13T12:52:32.123Z",
      "updated_at": "2016-03-13T12:52:32.123Z",
      "pricing_scheme": {
        "price": 150,
        "scheme_type": "scheme_type0",
        "price_brackets": [
          {
            "start_quantity": 59,
            "price": 3,
            "end_quantity": null,
            "overage_price": null
          },
          {
            "start_quantity": 60,
            "price": 2,
            "end_quantity": null,
            "overage_price": null
          }
        ],
        "minimum_price": null,
        "percentage": null
      },
      "description": "description8",
      "plan": {
        "id": "id6",
        "name": "name6",
        "description": "description4",
        "url": "url0",
        "statement_descriptor": "statement_descriptor6",
        "interval": "interval6",
        "interval_count": 88,
        "billing_type": "billing_type0",
        "payment_methods": [
          "payment_methods9",
          "payment_methods0",
          "payment_methods1"
        ],
        "installments": [
          125,
          126
        ],
        "status": "status2",
        "currency": "currency6",
        "created_at": "2016-03-13T12:52:32.123Z",
        "updated_at": "2016-03-13T12:52:32.123Z",
        "items": [
          {
            "id": "id3",
            "name": "name3",
            "status": "status5",
            "created_at": "2016-03-13T12:52:32.123Z",
            "updated_at": "2016-03-13T12:52:32.123Z",
            "pricing_scheme": {
              "price": 155,
              "scheme_type": "scheme_type5",
              "price_brackets": [
                {
                  "start_quantity": 54,
                  "price": 8,
                  "end_quantity": null,
                  "overage_price": null
                }
              ],
              "minimum_price": null,
              "percentage": null
            },
            "description": "description3",
            "plan": {
              "id": "id1",
              "name": "name1",
              "description": "description9",
              "url": "url5",
              "statement_descriptor": "statement_descriptor1",
              "interval": "interval1",
              "interval_count": 83,
              "billing_type": "billing_type5",
              "payment_methods": [
                "payment_methods4"
              ],
              "installments": [
                120
              ],
              "status": "status7",
              "currency": "currency9",
              "created_at": "2016-03-13T12:52:32.123Z",
              "updated_at": "2016-03-13T12:52:32.123Z",
              "items": [],
              "billing_days": [
                142,
                143
              ],
              "shippable": true,
              "metadata": {
                "key0": "metadata2",
                "key1": "metadata3"
              },
              "trial_period_days": null,
              "minimum_price": null,
              "deleted_at": null
            },
            "quantity": null,
            "cycles": null,
            "deleted_at": null
          }
        ],
        "billing_days": [
          119
        ],
        "shippable": false,
        "metadata": {
          "key0": "metadata7"
        },
        "trial_period_days": null,
        "minimum_price": null,
        "deleted_at": null
      },
      "quantity": null,
      "cycles": null,
      "deleted_at": null
    }
  ],
  "billing_days": [
    143,
    144,
    145
  ],
  "shippable": false,
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  },
  "trial_period_days": null,
  "minimum_price": null,
  "deleted_at": null
}
```

