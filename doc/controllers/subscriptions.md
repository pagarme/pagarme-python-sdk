# Subscriptions

```python
subscriptions_controller = client.subscriptions
```

## Class Name

`SubscriptionsController`

## Methods

* [Cancel Subscription](../../doc/controllers/subscriptions.md#cancel-subscription)
* [Create an Usage](../../doc/controllers/subscriptions.md#create-an-usage)
* [Create Discount](../../doc/controllers/subscriptions.md#create-discount)
* [Create Increment](../../doc/controllers/subscriptions.md#create-increment)
* [Create Subscription](../../doc/controllers/subscriptions.md#create-subscription)
* [Create Subscription Item](../../doc/controllers/subscriptions.md#create-subscription-item)
* [Create Usage](../../doc/controllers/subscriptions.md#create-usage)
* [Delete Discount](../../doc/controllers/subscriptions.md#delete-discount)
* [Delete Increment](../../doc/controllers/subscriptions.md#delete-increment)
* [Delete Subscription Item](../../doc/controllers/subscriptions.md#delete-subscription-item)
* [Delete Usage](../../doc/controllers/subscriptions.md#delete-usage)
* [Get Discount by Id](../../doc/controllers/subscriptions.md#get-discount-by-id)
* [Get Discounts](../../doc/controllers/subscriptions.md#get-discounts)
* [Get Increment by Id](../../doc/controllers/subscriptions.md#get-increment-by-id)
* [Get Increments](../../doc/controllers/subscriptions.md#get-increments)
* [Get Subscription](../../doc/controllers/subscriptions.md#get-subscription)
* [Get Subscription Cycle by Id](../../doc/controllers/subscriptions.md#get-subscription-cycle-by-id)
* [Get Subscription Cycles](../../doc/controllers/subscriptions.md#get-subscription-cycles)
* [Get Subscription Item](../../doc/controllers/subscriptions.md#get-subscription-item)
* [Get Subscription Items](../../doc/controllers/subscriptions.md#get-subscription-items)
* [Get Subscriptions](../../doc/controllers/subscriptions.md#get-subscriptions)
* [Get Usage Report](../../doc/controllers/subscriptions.md#get-usage-report)
* [Get Usages](../../doc/controllers/subscriptions.md#get-usages)
* [Renew Subscription](../../doc/controllers/subscriptions.md#renew-subscription)
* [Update Current Cycle Status](../../doc/controllers/subscriptions.md#update-current-cycle-status)
* [Update Latest Period End At](../../doc/controllers/subscriptions.md#update-latest-period-end-at)
* [Update Split Subscription](../../doc/controllers/subscriptions.md#update-split-subscription)
* [Update Subscription Affiliation Id](../../doc/controllers/subscriptions.md#update-subscription-affiliation-id)
* [Update Subscription Billing Date](../../doc/controllers/subscriptions.md#update-subscription-billing-date)
* [Update Subscription Card](../../doc/controllers/subscriptions.md#update-subscription-card)
* [Update Subscription Due Days](../../doc/controllers/subscriptions.md#update-subscription-due-days)
* [Update Subscription Item](../../doc/controllers/subscriptions.md#update-subscription-item)
* [Update Subscription Metadata](../../doc/controllers/subscriptions.md#update-subscription-metadata)
* [Update Subscription Minium Price](../../doc/controllers/subscriptions.md#update-subscription-minium-price)
* [Update Subscription Payment Method](../../doc/controllers/subscriptions.md#update-subscription-payment-method)
* [Update Subscription Start At](../../doc/controllers/subscriptions.md#update-subscription-start-at)


# Cancel Subscription

Cancels a subscription

```python
def cancel_subscription(self,
                       subscription_id,
                       request=None,
                       idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `request` | [`CreateCancelSubscriptionRequest`](../../doc/models/create-cancel-subscription-request.md) | Body, Optional | Request for cancelling a subscription |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = CreateCancelSubscriptionRequest(
    cancel_pending_invoices=True
)

result = subscriptions_controller.cancel_subscription(
    subscription_id,
    request=request
)
print(result)
```


# Create an Usage

Create Usage

```python
def create_an_usage(self,
                   subscription_id,
                   item_id,
                   idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `item_id` | `str` | Template, Required | Item id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetUsageResponse`](../../doc/models/get-usage-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

item_id = 'item_id0'

result = subscriptions_controller.create_an_usage(
    subscription_id,
    item_id
)
print(result)
```


# Create Discount

Creates a discount

```python
def create_discount(self,
                   subscription_id,
                   request,
                   idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `request` | [`CreateDiscountRequest`](../../doc/models/create-discount-request.md) | Body, Required | Request for creating a discount |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetDiscountResponse`](../../doc/models/get-discount-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = CreateDiscountRequest(
    value=185.28,
    discount_type='discount_type4',
    item_id='item_id6'
)

result = subscriptions_controller.create_discount(
    subscription_id,
    request
)
print(result)
```


# Create Increment

Creates a increment

```python
def create_increment(self,
                    subscription_id,
                    request,
                    idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `request` | [`CreateIncrementRequest`](../../doc/models/create-increment-request.md) | Body, Required | Request for creating a increment |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetIncrementResponse`](../../doc/models/get-increment-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = CreateIncrementRequest(
    value=185.28,
    increment_type='increment_type8',
    item_id='item_id6'
)

result = subscriptions_controller.create_increment(
    subscription_id,
    request
)
print(result)
```


# Create Subscription

Creates a new subscription

```python
def create_subscription(self,
                       body,
                       idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateSubscriptionRequest`](../../doc/models/create-subscription-request.md) | Body, Required | Request for creating a subscription |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
body = CreateSubscriptionRequest(
    customer=CreateCustomerRequest(
        name='Tony Stark',
        email=None,
        document=None,
        mtype=None,
        address=CreateAddressRequest(
            street=None,
            number=None,
            zip_code=None,
            neighborhood=None,
            city=None,
            state=None,
            country=None,
            complement=None,
            line_1=None,
            line_2=None
        ),
        metadata={},
        phones=CreatePhonesRequest(),
        code=None
    ),
    card=CreateCardRequest(
        mtype='credit'
    ),
    code=None,
    payment_method=None,
    billing_type=None,
    statement_descriptor=None,
    description=None,
    currency=None,
    interval=None,
    interval_count=None,
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type=None
    ),
    items=[
        CreateSubscriptionItemRequest(
            description=None,
            pricing_scheme=CreatePricingSchemeRequest(
                scheme_type=None
            ),
            id=None,
            plan_item_id=None,
            discounts=[
                None
            ],
            name=None
        )
    ],
    shipping=CreateShippingRequest(
        amount=None,
        description=None,
        recipient_name=None,
        recipient_phone=None,
        address_id=None,
        address=CreateAddressRequest(
            street=None,
            number=None,
            zip_code=None,
            neighborhood=None,
            city=None,
            state=None,
            country=None,
            complement=None,
            line_1=None,
            line_2=None
        ),
        mtype=None
    ),
    discounts=[
        None
    ],
    metadata={},
    increments=[
        None
    ]
)

result = subscriptions_controller.create_subscription(body)
print(result)
```


# Create Subscription Item

Creates a new Subscription item

```python
def create_subscription_item(self,
                            subscription_id,
                            request,
                            idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `request` | [`CreateSubscriptionItemRequest`](../../doc/models/create-subscription-item-request.md) | Body, Required | Request for creating a subscription item |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = CreateSubscriptionItemRequest(
    description=None,
    pricing_scheme=CreatePricingSchemeRequest(
        scheme_type=None
    ),
    id=None,
    plan_item_id=None,
    discounts=[
        None
    ],
    name=None
)

result = subscriptions_controller.create_subscription_item(
    subscription_id,
    request
)
print(result)
```


# Create Usage

Creates a usage

```python
def create_usage(self,
                subscription_id,
                item_id,
                body,
                idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |
| `item_id` | `str` | Template, Required | Item id |
| `body` | [`CreateUsageRequest`](../../doc/models/create-usage-request.md) | Body, Required | Request for creating a usage |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetUsageResponse`](../../doc/models/get-usage-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

item_id = 'item_id0'

body = CreateUsageRequest(
    quantity=156,
    description='description4',
    used_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

result = subscriptions_controller.create_usage(
    subscription_id,
    item_id,
    body
)
print(result)
```


# Delete Discount

Deletes a discount

```python
def delete_discount(self,
                   subscription_id,
                   discount_id,
                   idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `discount_id` | `str` | Template, Required | Discount Id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetDiscountResponse`](../../doc/models/get-discount-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

discount_id = 'discount_id8'

result = subscriptions_controller.delete_discount(
    subscription_id,
    discount_id
)
print(result)
```


# Delete Increment

Deletes a increment

```python
def delete_increment(self,
                    subscription_id,
                    increment_id,
                    idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `increment_id` | `str` | Template, Required | Increment id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetIncrementResponse`](../../doc/models/get-increment-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

increment_id = 'increment_id8'

result = subscriptions_controller.delete_increment(
    subscription_id,
    increment_id
)
print(result)
```


# Delete Subscription Item

Deletes a subscription item

```python
def delete_subscription_item(self,
                            subscription_id,
                            subscription_item_id,
                            idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `subscription_item_id` | `str` | Template, Required | Subscription item id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

subscription_item_id = 'subscription_item_id4'

result = subscriptions_controller.delete_subscription_item(
    subscription_id,
    subscription_item_id
)
print(result)
```


# Delete Usage

Deletes a usage

```python
def delete_usage(self,
                subscription_id,
                item_id,
                usage_id,
                idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `item_id` | `str` | Template, Required | The subscription item id |
| `usage_id` | `str` | Template, Required | The usage id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetUsageResponse`](../../doc/models/get-usage-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

item_id = 'item_id0'

usage_id = 'usage_id0'

result = subscriptions_controller.delete_usage(
    subscription_id,
    item_id,
    usage_id
)
print(result)
```


# Get Discount by Id

```python
def get_discount_by_id(self,
                      subscription_id,
                      discount_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `discount_id` | `str` | Template, Required | - |

## Response Type

**200**

[`GetDiscountResponse`](../../doc/models/get-discount-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

discount_id = 'discountId0'

result = subscriptions_controller.get_discount_by_id(
    subscription_id,
    discount_id
)
print(result)
```


# Get Discounts

```python
def get_discounts(self,
                 subscription_id,
                 page,
                 size)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `page` | `int` | Query, Required | Page number |
| `size` | `int` | Query, Required | Page size |

## Response Type

**200**

[`ListDiscountsResponse`](../../doc/models/list-discounts-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

page = 30

size = 18

result = subscriptions_controller.get_discounts(
    subscription_id,
    page,
    size
)
print(result)
```


# Get Increment by Id

```python
def get_increment_by_id(self,
                       subscription_id,
                       increment_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription Id |
| `increment_id` | `str` | Template, Required | The increment Id |

## Response Type

**200**

[`GetIncrementResponse`](../../doc/models/get-increment-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

increment_id = 'increment_id8'

result = subscriptions_controller.get_increment_by_id(
    subscription_id,
    increment_id
)
print(result)
```


# Get Increments

```python
def get_increments(self,
                  subscription_id,
                  page=None,
                  size=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |

## Response Type

**200**

[`ListIncrementsResponse`](../../doc/models/list-increments-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_controller.get_increments(subscription_id)
print(result)
```


# Get Subscription

Gets a subscription

```python
def get_subscription(self,
                    subscription_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_controller.get_subscription(subscription_id)
print(result)
```


# Get Subscription Cycle by Id

```python
def get_subscription_cycle_by_id(self,
                                subscription_id,
                                cycle_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `cycle_id` | `str` | Template, Required | - |

## Response Type

**200**

[`GetPeriodResponse`](../../doc/models/get-period-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

cycle_id = 'cycleId0'

result = subscriptions_controller.get_subscription_cycle_by_id(
    subscription_id,
    cycle_id
)
print(result)
```


# Get Subscription Cycles

```python
def get_subscription_cycles(self,
                           subscription_id,
                           page,
                           size)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |
| `page` | `str` | Query, Required | Page number |
| `size` | `str` | Query, Required | Page size |

## Response Type

**200**

[`ListCyclesResponse`](../../doc/models/list-cycles-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

page = 'page8'

size = 'size0'

result = subscriptions_controller.get_subscription_cycles(
    subscription_id,
    page,
    size
)
print(result)
```


# Get Subscription Item

Get Subscription Item

```python
def get_subscription_item(self,
                         subscription_id,
                         item_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |
| `item_id` | `str` | Template, Required | Item id |

## Response Type

**200**

[`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

item_id = 'item_id0'

result = subscriptions_controller.get_subscription_item(
    subscription_id,
    item_id
)
print(result)
```


# Get Subscription Items

Get Subscription Items

```python
def get_subscription_items(self,
                          subscription_id,
                          page=None,
                          size=None,
                          name=None,
                          code=None,
                          status=None,
                          description=None,
                          created_since=None,
                          created_until=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `name` | `str` | Query, Optional | The item name |
| `code` | `str` | Query, Optional | Identification code in the client system |
| `status` | `str` | Query, Optional | The item statis |
| `description` | `str` | Query, Optional | The item description |
| `created_since` | `str` | Query, Optional | Filter for item's creation date start range |
| `created_until` | `str` | Query, Optional | Filter for item's creation date end range |

## Response Type

**200**

[`ListSubscriptionItemsResponse`](../../doc/models/list-subscription-items-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_controller.get_subscription_items(subscription_id)
print(result)
```


# Get Subscriptions

Gets all subscriptions

```python
def get_subscriptions(self,
                     page=None,
                     size=None,
                     code=None,
                     billing_type=None,
                     customer_id=None,
                     plan_id=None,
                     card_id=None,
                     status=None,
                     next_billing_since=None,
                     next_billing_until=None,
                     created_since=None,
                     created_until=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `code` | `str` | Query, Optional | Filter for subscription's code |
| `billing_type` | `str` | Query, Optional | Filter for subscription's billing type |
| `customer_id` | `str` | Query, Optional | Filter for subscription's customer id |
| `plan_id` | `str` | Query, Optional | Filter for subscription's plan id |
| `card_id` | `str` | Query, Optional | Filter for subscription's card id |
| `status` | `str` | Query, Optional | Filter for subscription's status |
| `next_billing_since` | `datetime` | Query, Optional | Filter for subscription's next billing date start range |
| `next_billing_until` | `datetime` | Query, Optional | Filter for subscription's next billing date end range |
| `created_since` | `datetime` | Query, Optional | Filter for subscription's creation date start range |
| `created_until` | `datetime` | Query, Optional | Filter for subscriptions creation date end range |

## Response Type

**200**

[`ListSubscriptionsResponse`](../../doc/models/list-subscriptions-response.md)

## Example Usage

```python
result = subscriptions_controller.get_subscriptions()
print(result)
```


# Get Usage Report

```python
def get_usage_report(self,
                    subscription_id,
                    period_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription Id |
| `period_id` | `str` | Template, Required | The period Id |

## Response Type

**200**

[`GetUsageReportResponse`](../../doc/models/get-usage-report-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

period_id = 'period_id0'

result = subscriptions_controller.get_usage_report(
    subscription_id,
    period_id
)
print(result)
```


# Get Usages

Lists all usages from a subscription item

```python
def get_usages(self,
              subscription_id,
              item_id,
              page=None,
              size=None,
              code=None,
              group=None,
              used_since=None,
              used_until=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `item_id` | `str` | Template, Required | The subscription item id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `code` | `str` | Query, Optional | Identification code in the client system |
| `group` | `str` | Query, Optional | Identification group in the client system |
| `used_since` | `datetime` | Query, Optional | - |
| `used_until` | `datetime` | Query, Optional | - |

## Response Type

**200**

[`ListUsagesResponse`](../../doc/models/list-usages-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

item_id = 'item_id0'

result = subscriptions_controller.get_usages(
    subscription_id,
    item_id
)
print(result)
```


# Renew Subscription

```python
def renew_subscription(self,
                      subscription_id,
                      idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | - |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetPeriodResponse`](../../doc/models/get-period-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_controller.renew_subscription(subscription_id)
print(result)
```


# Update Current Cycle Status

```python
def update_current_cycle_status(self,
                               subscription_id,
                               request,
                               idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |
| `request` | [`UpdateCurrentCycleStatusRequest`](../../doc/models/update-current-cycle-status-request.md) | Body, Required | Request for updating the end date of the subscription current status |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

`void`

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateCurrentCycleStatusRequest(
    status='status8'
)

subscriptions_controller.update_current_cycle_status(
    subscription_id,
    request
)
```


# Update Latest Period End At

```python
def update_latest_period_end_at(self,
                               subscription_id,
                               request,
                               idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | - |
| `request` | [`UpdateCurrentCycleEndDateRequest`](../../doc/models/update-current-cycle-end-date-request.md) | Body, Required | Request for updating the end date of the current signature cycle |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateCurrentCycleEndDateRequest()

result = subscriptions_controller.update_latest_period_end_at(
    subscription_id,
    request
)
print(result)
```


# Update Split Subscription

```python
def update_split_subscription(self,
                             id,
                             request)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | Subscription's id |
| `request` | [`UpdateSubscriptionSplitRequest`](../../doc/models/update-subscription-split-request.md) | Body, Required | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
id = 'id0'

request = UpdateSubscriptionSplitRequest(
    enabled=None,
    rules=[
        None
    ]
)

result = subscriptions_controller.update_split_subscription(
    id,
    request
)
print(result)
```


# Update Subscription Affiliation Id

```python
def update_subscription_affiliation_id(self,
                                      subscription_id,
                                      request,
                                      idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | - |
| `request` | [`UpdateSubscriptionAffiliationIdRequest`](../../doc/models/update-subscription-affiliation-id-request.md) | Body, Required | Request for updating a subscription affiliation id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateSubscriptionAffiliationIdRequest(
    gateway_affiliation_id='gateway_affiliation_id2'
)

result = subscriptions_controller.update_subscription_affiliation_id(
    subscription_id,
    request
)
print(result)
```


# Update Subscription Billing Date

Updates the billing date from a subscription

```python
def update_subscription_billing_date(self,
                                    subscription_id,
                                    request,
                                    idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `request` | [`UpdateSubscriptionBillingDateRequest`](../../doc/models/update-subscription-billing-date-request.md) | Body, Required | Request for updating the subscription billing date |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateSubscriptionBillingDateRequest(
    next_billing_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

result = subscriptions_controller.update_subscription_billing_date(
    subscription_id,
    request
)
print(result)
```


# Update Subscription Card

Updates the credit card from a subscription

```python
def update_subscription_card(self,
                            subscription_id,
                            request,
                            idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `request` | [`UpdateSubscriptionCardRequest`](../../doc/models/update-subscription-card-request.md) | Body, Required | Request for updating a card |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateSubscriptionCardRequest(
    card=CreateCardRequest(
        mtype='credit'
    ),
    card_id=None
)

result = subscriptions_controller.update_subscription_card(
    subscription_id,
    request
)
print(result)
```


# Update Subscription Due Days

Updates the boleto due days from a subscription

```python
def update_subscription_due_days(self,
                                subscription_id,
                                request,
                                idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |
| `request` | [`UpdateSubscriptionDueDaysRequest`](../../doc/models/update-subscription-due-days-request.md) | Body, Required | - |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateSubscriptionDueDaysRequest(
    boleto_due_days=226
)

result = subscriptions_controller.update_subscription_due_days(
    subscription_id,
    request
)
print(result)
```


# Update Subscription Item

Updates a subscription item

```python
def update_subscription_item(self,
                            subscription_id,
                            item_id,
                            body,
                            idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |
| `item_id` | `str` | Template, Required | Item id |
| `body` | [`UpdateSubscriptionItemRequest`](../../doc/models/update-subscription-item-request.md) | Body, Required | Request for updating a subscription item |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionItemResponse`](../../doc/models/get-subscription-item-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

item_id = 'item_id0'

body = UpdateSubscriptionItemRequest(
    description=None,
    status=None,
    pricing_scheme=UpdatePricingSchemeRequest(
        scheme_type=None,
        price_brackets=[
            None
        ]
    ),
    name=None
)

result = subscriptions_controller.update_subscription_item(
    subscription_id,
    item_id,
    body
)
print(result)
```


# Update Subscription Metadata

Updates the metadata from a subscription

```python
def update_subscription_metadata(self,
                                subscription_id,
                                request,
                                idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Request for updating the subscrption metadata |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateMetadataRequest(
    metadata={
        'key0': 'metadata3'
    }
)

result = subscriptions_controller.update_subscription_metadata(
    subscription_id,
    request
)
print(result)
```


# Update Subscription Minium Price

Atualização do valor mínimo da assinatura

```python
def update_subscription_minium_price(self,
                                    subscription_id,
                                    request,
                                    idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |
| `request` | [`UpdateSubscriptionMinimumPriceRequest`](../../doc/models/update-subscription-minimum-price-request.md) | Body, Required | Request da requisição com o valor mínimo que será configurado |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateSubscriptionMinimumPriceRequest()

result = subscriptions_controller.update_subscription_minium_price(
    subscription_id,
    request
)
print(result)
```


# Update Subscription Payment Method

Updates the payment method from a subscription

```python
def update_subscription_payment_method(self,
                                      subscription_id,
                                      request,
                                      idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription id |
| `request` | [`UpdateSubscriptionPaymentMethodRequest`](../../doc/models/update-subscription-payment-method-request.md) | Body, Required | Request for updating the paymentmethod from a subscription |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateSubscriptionPaymentMethodRequest(
    payment_method=None,
    card_id=None,
    card=CreateCardRequest(
        mtype='credit'
    )
)

result = subscriptions_controller.update_subscription_payment_method(
    subscription_id,
    request
)
print(result)
```


# Update Subscription Start At

Updates the start at date from a subscription

```python
def update_subscription_start_at(self,
                                subscription_id,
                                request,
                                idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The subscription id |
| `request` | [`UpdateSubscriptionStartAtRequest`](../../doc/models/update-subscription-start-at-request.md) | Body, Required | Request for updating the subscription start date |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetSubscriptionResponse`](../../doc/models/get-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

request = UpdateSubscriptionStartAtRequest(
    start_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

result = subscriptions_controller.update_subscription_start_at(
    subscription_id,
    request
)
print(result)
```

