# Plans

```python
plans_controller = client.plans
```

## Class Name

`PlansController`

## Methods

* [Get Plan](../../doc/controllers/plans.md#get-plan)
* [Update Plan](../../doc/controllers/plans.md#update-plan)
* [Update Plan Metadata](../../doc/controllers/plans.md#update-plan-metadata)
* [Delete Plan Item](../../doc/controllers/plans.md#delete-plan-item)
* [Get Plans](../../doc/controllers/plans.md#get-plans)
* [Get Plan Item](../../doc/controllers/plans.md#get-plan-item)
* [Delete Plan](../../doc/controllers/plans.md#delete-plan)
* [Update Plan Item](../../doc/controllers/plans.md#update-plan-item)
* [Create Plan Item](../../doc/controllers/plans.md#create-plan-item)
* [Create Plan](../../doc/controllers/plans.md#create-plan)


# Get Plan

Gets a plan

```python
def get_plan(self,
            plan_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Template, Required | Plan id |

## Response Type

[`GetPlanResponse`](../../doc/models/get-plan-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

result = plans_controller.get_plan(plan_id)
print(result)
```


# Update Plan

Updates a plan

```python
def update_plan(self,
               plan_id,
               request,
               idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Template, Required | Plan id |
| `request` | [`UpdatePlanRequest`](../../doc/models/update-plan-request.md) | Body, Required | Request for updating a plan |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetPlanResponse`](../../doc/models/get-plan-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

request = UpdatePlanRequest(
    name='name6',
    description='description6',
    installments=[
        151,
        152
    ],
    statement_descriptor='statement_descriptor6',
    currency='currency6',
    interval='interval4',
    interval_count=114,
    payment_methods=[
        'payment_methods1',
        'payment_methods0',
        'payment_methods9'
    ],
    billing_type='billing_type0',
    status='status8',
    shippable=False,
    billing_days=[
        115
    ],
    metadata={
        'key0': 'metadata3'
    }
)

result = plans_controller.update_plan(
    plan_id,
    request
)
print(result)
```


# Update Plan Metadata

Updates the metadata from a plan

```python
def update_plan_metadata(self,
                        plan_id,
                        request,
                        idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Template, Required | The plan id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Request for updating the plan metadata |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetPlanResponse`](../../doc/models/get-plan-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

request = UpdateMetadataRequest(
    metadata={
        'key0': 'metadata3'
    }
)

result = plans_controller.update_plan_metadata(
    plan_id,
    request
)
print(result)
```


# Delete Plan Item

Removes an item from a plan

```python
def delete_plan_item(self,
                    plan_id,
                    plan_item_id,
                    idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Template, Required | Plan id |
| `plan_item_id` | `str` | Template, Required | Plan item id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetPlanItemResponse`](../../doc/models/get-plan-item-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

plan_item_id = 'plan_item_id0'

result = plans_controller.delete_plan_item(
    plan_id,
    plan_item_id
)
print(result)
```


# Get Plans

Gets all plans

```python
def get_plans(self,
             page=None,
             size=None,
             name=None,
             status=None,
             billing_type=None,
             created_since=None,
             created_until=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `name` | `str` | Query, Optional | Filter for Plan's name |
| `status` | `str` | Query, Optional | Filter for Plan's status |
| `billing_type` | `str` | Query, Optional | Filter for plan's billing type |
| `created_since` | `datetime` | Query, Optional | Filter for plan's creation date start range |
| `created_until` | `datetime` | Query, Optional | Filter for plan's creation date end range |

## Response Type

[`ListPlansResponse`](../../doc/models/list-plans-response.md)

## Example Usage

```python
result = plans_controller.get_plans()
print(result)
```


# Get Plan Item

Gets a plan item

```python
def get_plan_item(self,
                 plan_id,
                 plan_item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Template, Required | Plan id |
| `plan_item_id` | `str` | Template, Required | Plan item id |

## Response Type

[`GetPlanItemResponse`](../../doc/models/get-plan-item-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

plan_item_id = 'plan_item_id0'

result = plans_controller.get_plan_item(
    plan_id,
    plan_item_id
)
print(result)
```


# Delete Plan

Deletes a plan

```python
def delete_plan(self,
               plan_id,
               idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Template, Required | Plan id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetPlanResponse`](../../doc/models/get-plan-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

result = plans_controller.delete_plan(plan_id)
print(result)
```


# Update Plan Item

Updates a plan item

```python
def update_plan_item(self,
                    plan_id,
                    plan_item_id,
                    body,
                    idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Template, Required | Plan id |
| `plan_item_id` | `str` | Template, Required | Plan item id |
| `body` | [`UpdatePlanItemRequest`](../../doc/models/update-plan-item-request.md) | Body, Required | Request for updating the plan item |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetPlanItemResponse`](../../doc/models/get-plan-item-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

plan_item_id = 'plan_item_id0'

body = UpdatePlanItemRequest(
    name='name6',
    description='description4',
    status='status2',
    pricing_scheme=UpdatePricingSchemeRequest(
        scheme_type='scheme_type8',
        price_brackets=[
            UpdatePriceBracketRequest(
                start_quantity=144,
                price=174
            )
        ]
    )
)

result = plans_controller.update_plan_item(
    plan_id,
    plan_item_id,
    body
)
print(result)
```


# Create Plan Item

Adds a new item to a plan

```python
def create_plan_item(self,
                    plan_id,
                    request,
                    idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `str` | Template, Required | Plan id |
| `request` | [`CreatePlanItemRequest`](../../doc/models/create-plan-item-request.md) | Body, Required | Request for creating a plan item |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetPlanItemResponse`](../../doc/models/get-plan-item-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

request = CreatePlanItemRequest(
    name='name6',
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type='scheme_type8'
    ),
    id='id6',
    description='description6'
)

result = plans_controller.create_plan_item(
    plan_id,
    request
)
print(result)
```


# Create Plan

Creates a new plan

```python
def create_plan(self,
               body,
               idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreatePlanRequest`](../../doc/models/create-plan-request.md) | Body, Required | Request for creating a plan |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetPlanResponse`](../../doc/models/get-plan-response.md)

## Example Usage

```python
body = CreatePlanRequest(
    name='name6',
    description='description4',
    statement_descriptor='statement_descriptor6',
    items=[
        CreatePlanItemRequest(
            name='name8',
            pricing_scheme=CreatePricingSchemeRequest(
                scheme_type='scheme_type8'
            ),
            id='id8',
            description='description2'
        )
    ],
    shippable=False,
    payment_methods=[
        'payment_methods9'
    ],
    installments=[
        207
    ],
    currency='currency6',
    interval='interval6',
    interval_count=170,
    billing_days=[
        201,
        200
    ],
    billing_type='billing_type0',
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type='scheme_type8'
    ),
    metadata={
        'key0': 'metadata7',
        'key1': 'metadata8'
    }
)

result = plans_controller.create_plan(body)
print(result)
```

