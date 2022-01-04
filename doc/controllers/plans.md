# Plans

```python
plans_controller = client.plans
```

## Class Name

`PlansController`

## Methods

* [Get Plan](/doc/controllers/plans.md#get-plan)
* [Update Plan](/doc/controllers/plans.md#update-plan)
* [Update Plan Metadata](/doc/controllers/plans.md#update-plan-metadata)
* [Delete Plan Item](/doc/controllers/plans.md#delete-plan-item)
* [Get Plans](/doc/controllers/plans.md#get-plans)
* [Get Plan Item](/doc/controllers/plans.md#get-plan-item)
* [Delete Plan](/doc/controllers/plans.md#delete-plan)
* [Update Plan Item](/doc/controllers/plans.md#update-plan-item)
* [Create Plan Item](/doc/controllers/plans.md#create-plan-item)
* [Create Plan](/doc/controllers/plans.md#create-plan)


# Get Plan

Gets a plan

```python
def get_plan(self,
            plan_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_id` | `string` | Template, Required | Plan id |

## Response Type

[`GetPlanResponse`](/doc/models/get-plan-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

result = plans_controller.get_plan(plan_id)
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
| `plan_id` | `string` | Template, Required | Plan id |
| `request` | [`UpdatePlanRequest`](/doc/models/update-plan-request.md) | Body, Required | Request for updating a plan |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetPlanResponse`](/doc/models/get-plan-response.md)

## Example Usage

```python
plan_id = 'plan_id8'
request = UpdatePlanRequest()
request.name = 'name6'
request.description = 'description6'
request.installments = [151, 152]
request.statement_descriptor = 'statement_descriptor6'
request.currency = 'currency6'
request.interval = 'interval4'
request.interval_count = 114
request.payment_methods = ['payment_methods1', 'payment_methods0', 'payment_methods9']
request.billing_type = 'billing_type0'
request.status = 'status8'
request.shippable = False
request.billing_days = [115]
request.metadata = {'key0' : 'metadata3' } 

result = plans_controller.update_plan(plan_id, request)
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
| `plan_id` | `string` | Template, Required | The plan id |
| `request` | [`UpdateMetadataRequest`](/doc/models/update-metadata-request.md) | Body, Required | Request for updating the plan metadata |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetPlanResponse`](/doc/models/get-plan-response.md)

## Example Usage

```python
plan_id = 'plan_id8'
request = UpdateMetadataRequest()
request.metadata = {'key0' : 'metadata3' } 

result = plans_controller.update_plan_metadata(plan_id, request)
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
| `plan_id` | `string` | Template, Required | Plan id |
| `plan_item_id` | `string` | Template, Required | Plan item id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetPlanItemResponse`](/doc/models/get-plan-item-response.md)

## Example Usage

```python
plan_id = 'plan_id8'
plan_item_id = 'plan_item_id0'

result = plans_controller.delete_plan_item(plan_id, plan_item_id)
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
| `name` | `string` | Query, Optional | Filter for Plan's name |
| `status` | `string` | Query, Optional | Filter for Plan's status |
| `billing_type` | `string` | Query, Optional | Filter for plan's billing type |
| `created_since` | `datetime` | Query, Optional | Filter for plan's creation date start range |
| `created_until` | `datetime` | Query, Optional | Filter for plan's creation date end range |

## Response Type

[`ListPlansResponse`](/doc/models/list-plans-response.md)

## Example Usage

```python
result = plans_controller.get_plans()
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
| `plan_id` | `string` | Template, Required | Plan id |
| `plan_item_id` | `string` | Template, Required | Plan item id |

## Response Type

[`GetPlanItemResponse`](/doc/models/get-plan-item-response.md)

## Example Usage

```python
plan_id = 'plan_id8'
plan_item_id = 'plan_item_id0'

result = plans_controller.get_plan_item(plan_id, plan_item_id)
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
| `plan_id` | `string` | Template, Required | Plan id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetPlanResponse`](/doc/models/get-plan-response.md)

## Example Usage

```python
plan_id = 'plan_id8'

result = plans_controller.delete_plan(plan_id)
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
| `plan_id` | `string` | Template, Required | Plan id |
| `plan_item_id` | `string` | Template, Required | Plan item id |
| `body` | [`UpdatePlanItemRequest`](/doc/models/update-plan-item-request.md) | Body, Required | Request for updating the plan item |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetPlanItemResponse`](/doc/models/get-plan-item-response.md)

## Example Usage

```python
plan_id = 'plan_id8'
plan_item_id = 'plan_item_id0'
body = UpdatePlanItemRequest()
body.name = 'name6'
body.description = 'description4'
body.status = 'status2'
body.pricing_scheme = UpdatePricingSchemeRequest()
body.pricing_scheme.scheme_type = 'scheme_type2'
body.pricing_scheme.price_brackets = []

body.pricing_scheme.price_brackets.append(UpdatePriceBracketRequest())
body.pricing_scheme.price_brackets[0].start_quantity = 31
body.pricing_scheme.price_brackets[0].price = 225

body.pricing_scheme.price_brackets.append(UpdatePriceBracketRequest())
body.pricing_scheme.price_brackets[1].start_quantity = 32
body.pricing_scheme.price_brackets[1].price = 226


result = plans_controller.update_plan_item(plan_id, plan_item_id, body)
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
| `plan_id` | `string` | Template, Required | Plan id |
| `request` | [`CreatePlanItemRequest`](/doc/models/create-plan-item-request.md) | Body, Required | Request for creating a plan item |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetPlanItemResponse`](/doc/models/get-plan-item-response.md)

## Example Usage

```python
plan_id = 'plan_id8'
request = CreatePlanItemRequest()
request.name = 'name6'
request.pricing_scheme = CreatePricingSchemeRequest()
request.pricing_scheme.scheme_type = 'scheme_type2'
request.pricing_scheme.price_brackets = []

request.pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
request.pricing_scheme.price_brackets[0].start_quantity = 87
request.pricing_scheme.price_brackets[0].price = 231

request.id = 'id6'
request.description = 'description6'

result = plans_controller.create_plan_item(plan_id, request)
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
| `body` | [`CreatePlanRequest`](/doc/models/create-plan-request.md) | Body, Required | Request for creating a plan |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetPlanResponse`](/doc/models/get-plan-response.md)

## Example Usage

```python
body = CreatePlanRequest()
body.name = 'name6'
body.description = 'description4'
body.statement_descriptor = 'statement_descriptor6'
body.items = []

body.items.append(CreatePlanItemRequest())
body.items[0].name = 'name3'
body.items[0].pricing_scheme = CreatePricingSchemeRequest()
body.items[0].pricing_scheme.scheme_type = 'scheme_type5'
body.items[0].pricing_scheme.price_brackets = []

body.items[0].pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
body.items[0].pricing_scheme.price_brackets[0].start_quantity = 228
body.items[0].pricing_scheme.price_brackets[0].price = 90

body.items[0].pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
body.items[0].pricing_scheme.price_brackets[1].start_quantity = 229
body.items[0].pricing_scheme.price_brackets[1].price = 89

body.items[0].id = 'id3'
body.items[0].description = 'description3'

body.items.append(CreatePlanItemRequest())
body.items[1].name = 'name4'
body.items[1].pricing_scheme = CreatePricingSchemeRequest()
body.items[1].pricing_scheme.scheme_type = 'scheme_type4'
body.items[1].pricing_scheme.price_brackets = []

body.items[1].pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
body.items[1].pricing_scheme.price_brackets[0].start_quantity = 227
body.items[1].pricing_scheme.price_brackets[0].price = 91

body.items[1].id = 'id4'
body.items[1].description = 'description4'

body.items.append(CreatePlanItemRequest())
body.items[2].name = 'name5'
body.items[2].pricing_scheme = CreatePricingSchemeRequest()
body.items[2].pricing_scheme.scheme_type = 'scheme_type3'
body.items[2].pricing_scheme.price_brackets = []

body.items[2].pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
body.items[2].pricing_scheme.price_brackets[0].start_quantity = 226
body.items[2].pricing_scheme.price_brackets[0].price = 92

body.items[2].pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
body.items[2].pricing_scheme.price_brackets[1].start_quantity = 227
body.items[2].pricing_scheme.price_brackets[1].price = 91

body.items[2].pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
body.items[2].pricing_scheme.price_brackets[2].start_quantity = 228
body.items[2].pricing_scheme.price_brackets[2].price = 90

body.items[2].id = 'id5'
body.items[2].description = 'description5'

body.shippable = False
body.payment_methods = ['payment_methods9']
body.installments = [207]
body.currency = 'currency6'
body.interval = 'interval6'
body.interval_count = 170
body.billing_days = [201, 200]
body.billing_type = 'billing_type0'
body.pricing_scheme = CreatePricingSchemeRequest()
body.pricing_scheme.scheme_type = 'scheme_type2'
body.pricing_scheme.price_brackets = []

body.pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
body.pricing_scheme.price_brackets[0].start_quantity = 31
body.pricing_scheme.price_brackets[0].price = 225

body.pricing_scheme.price_brackets.append(CreatePriceBracketRequest())
body.pricing_scheme.price_brackets[1].start_quantity = 32
body.pricing_scheme.price_brackets[1].price = 226

body.metadata = {'key0' : 'metadata7', 'key1' : 'metadata8' } 

result = plans_controller.create_plan(body)
```

