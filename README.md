# Getting started

Pagarme API

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=PagarmeCoreApi-Python)


## How to Use

The following section explains how to use the Pagarmecoreapi SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=PagarmeCoreApi-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=PagarmeCoreApi-Python&projectName=pagarmecoreapi)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=PagarmeCoreApi-Python&projectName=pagarmecoreapi)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=PagarmeCoreApi-Python&projectName=pagarmecoreapi)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from pagarmecoreapi.pagarmecoreapi_client import PagarmecoreapiClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=PagarmeCoreApi-Python&libraryName=pagarmecoreapi.pagarmecoreapi_client&projectName=pagarmecoreapi&className=PagarmecoreapiClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=PagarmeCoreApi-Python&libraryName=pagarmecoreapi.pagarmecoreapi_client&projectName=pagarmecoreapi&className=PagarmecoreapiClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password | The password to use with basic authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = PagarmecoreapiClient(basic_auth_user_name, basic_auth_password)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [PlansController](#plans_controller)
* [SubscriptionsController](#subscriptions_controller)
* [OrdersController](#orders_controller)
* [InvoicesController](#invoices_controller)
* [CustomersController](#customers_controller)
* [ChargesController](#charges_controller)
* [TransfersController](#transfers_controller)
* [RecipientsController](#recipients_controller)
* [TokensController](#tokens_controller)
* [SellersController](#sellers_controller)
* [TransactionsController](#transactions_controller)

## <a name="plans_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PlansController") PlansController

### Get controller instance

An instance of the ``` PlansController ``` class can be accessed from the API Client.

```python
 plans_controller = client.plans
```

### <a name="get_plan"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.get_plan") get_plan

> Gets a plan

```python
def get_plan(self,
                 plan_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| planId |  ``` Required ```  | Plan id |



#### Example Usage

```python
plan_id = 'plan_id'

result = plans_controller.get_plan(plan_id)

```


### <a name="update_plan_metadata"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.update_plan_metadata") update_plan_metadata

> Updates the metadata from a plan

```python
def update_plan_metadata(self,
                             plan_id,
                             request,
                             idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| planId |  ``` Required ```  | The plan id |
| request |  ``` Required ```  | Request for updating the plan metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
plan_id = 'plan_id'
request = UpdateMetadataRequest()
idempotency_key = 'idempotency-key'

result = plans_controller.update_plan_metadata(plan_id, request, idempotency_key)

```


### <a name="update_plan_item"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.update_plan_item") update_plan_item

> Updates a plan item

```python
def update_plan_item(self,
                         plan_id,
                         plan_item_id,
                         body,
                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| planId |  ``` Required ```  | Plan id |
| planItemId |  ``` Required ```  | Plan item id |
| body |  ``` Required ```  | Request for updating the plan item |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
plan_id = 'plan_id'
plan_item_id = 'plan_item_id'
body = UpdatePlanItemRequest()
idempotency_key = 'idempotency-key'

result = plans_controller.update_plan_item(plan_id, plan_item_id, body, idempotency_key)

```


### <a name="create_plan_item"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.create_plan_item") create_plan_item

> Adds a new item to a plan

```python
def create_plan_item(self,
                         plan_id,
                         request,
                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| planId |  ``` Required ```  | Plan id |
| request |  ``` Required ```  | Request for creating a plan item |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
plan_id = 'plan_id'
request = CreatePlanItemRequest()
idempotency_key = 'idempotency-key'

result = plans_controller.create_plan_item(plan_id, request, idempotency_key)

```


### <a name="get_plan_item"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.get_plan_item") get_plan_item

> Gets a plan item

```python
def get_plan_item(self,
                      plan_id,
                      plan_item_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| planId |  ``` Required ```  | Plan id |
| planItemId |  ``` Required ```  | Plan item id |



#### Example Usage

```python
plan_id = 'plan_id'
plan_item_id = 'plan_item_id'

result = plans_controller.get_plan_item(plan_id, plan_item_id)

```


### <a name="create_plan"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.create_plan") create_plan

> Creates a new plan

```python
def create_plan(self,
                    body,
                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | Request for creating a plan |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = CreatePlanRequest()
idempotency_key = 'idempotency-key'

result = plans_controller.create_plan(body, idempotency_key)

```


### <a name="delete_plan_item"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.delete_plan_item") delete_plan_item

> Removes an item from a plan

```python
def delete_plan_item(self,
                         plan_id,
                         plan_item_id,
                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| planId |  ``` Required ```  | Plan id |
| planItemId |  ``` Required ```  | Plan item id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
plan_id = 'plan_id'
plan_item_id = 'plan_item_id'
idempotency_key = 'idempotency-key'

result = plans_controller.delete_plan_item(plan_id, plan_item_id, idempotency_key)

```


### <a name="get_plans"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.get_plans") get_plans

> Gets all plans

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

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| name |  ``` Optional ```  | Filter for Plan's name |
| status |  ``` Optional ```  | Filter for Plan's status |
| billingType |  ``` Optional ```  | Filter for plan's billing type |
| createdSince |  ``` Optional ```  | Filter for plan's creation date start range |
| createdUntil |  ``` Optional ```  | Filter for plan's creation date end range |



#### Example Usage

```python
page = 225
size = 225
name = 'name'
status = 'status'
billing_type = 'billing_type'
created_since = datetime.now()
created_until = datetime.now()

result = plans_controller.get_plans(page, size, name, status, billing_type, created_since, created_until)

```


### <a name="update_plan"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.update_plan") update_plan

> Updates a plan

```python
def update_plan(self,
                    plan_id,
                    request,
                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| planId |  ``` Required ```  | Plan id |
| request |  ``` Required ```  | Request for updating a plan |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
plan_id = 'plan_id'
request = UpdatePlanRequest()
idempotency_key = 'idempotency-key'

result = plans_controller.update_plan(plan_id, request, idempotency_key)

```


### <a name="delete_plan"></a>![Method: ](https://apidocs.io/img/method.png ".PlansController.delete_plan") delete_plan

> Deletes a plan

```python
def delete_plan(self,
                    plan_id,
                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| planId |  ``` Required ```  | Plan id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
plan_id = 'plan_id'
idempotency_key = 'idempotency-key'

result = plans_controller.delete_plan(plan_id, idempotency_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="subscriptions_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SubscriptionsController") SubscriptionsController

### Get controller instance

An instance of the ``` SubscriptionsController ``` class can be accessed from the API Client.

```python
 subscriptions_controller = client.subscriptions
```

### <a name="update_subscription_card"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_card") update_subscription_card

> Updates the credit card from a subscription

```python
def update_subscription_card(self,
                                 subscription_id,
                                 request,
                                 idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| request |  ``` Required ```  | Request for updating a card |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateSubscriptionCardRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_card(subscription_id, request, idempotency_key)

```


### <a name="delete_usage"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.delete_usage") delete_usage

> Deletes a usage

```python
def delete_usage(self,
                     subscription_id,
                     item_id,
                     usage_id,
                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| itemId |  ``` Required ```  | The subscription item id |
| usageId |  ``` Required ```  | The usage id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
item_id = 'item_id'
usage_id = 'usage_id'
idempotency_key = 'idempotency-key'

result = subscriptions_controller.delete_usage(subscription_id, item_id, usage_id, idempotency_key)

```


### <a name="create_discount"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.create_discount") create_discount

> Creates a discount

```python
def create_discount(self,
                        subscription_id,
                        request,
                        idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| request |  ``` Required ```  | Request for creating a discount |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = CreateDiscountRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.create_discount(subscription_id, request, idempotency_key)

```


### <a name="create_an_usage"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.create_an_usage") create_an_usage

> Create Usage

```python
def create_an_usage(self,
                        subscription_id,
                        item_id,
                        idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| itemId |  ``` Required ```  | Item id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
item_id = 'item_id'
idempotency_key = 'idempotency-key'

result = subscriptions_controller.create_an_usage(subscription_id, item_id, idempotency_key)

```


### <a name="update_current_cycle_status"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_current_cycle_status") update_current_cycle_status

> TODO: Add a method description

```python
def update_current_cycle_status(self,
                                    subscription_id,
                                    request,
                                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |
| request |  ``` Required ```  | Request for updating the end date of the subscription current status |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateCurrentCycleStatusRequest()
idempotency_key = 'idempotency-key'

subscriptions_controller.update_current_cycle_status(subscription_id, request, idempotency_key)

```


### <a name="update_subscription_payment_method"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_payment_method") update_subscription_payment_method

> Updates the payment method from a subscription

```python
def update_subscription_payment_method(self,
                                           subscription_id,
                                           request,
                                           idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| request |  ``` Required ```  | Request for updating the paymentmethod from a subscription |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateSubscriptionPaymentMethodRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_payment_method(subscription_id, request, idempotency_key)

```


### <a name="delete_discount"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.delete_discount") delete_discount

> Deletes a discount

```python
def delete_discount(self,
                        subscription_id,
                        discount_id,
                        idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| discountId |  ``` Required ```  | Discount Id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
discount_id = 'discount_id'
idempotency_key = 'idempotency-key'

result = subscriptions_controller.delete_discount(subscription_id, discount_id, idempotency_key)

```


### <a name="get_subscription_items"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_subscription_items") get_subscription_items

> Get Subscription Items

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

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| name |  ``` Optional ```  | The item name |
| code |  ``` Optional ```  | Identification code in the client system |
| status |  ``` Optional ```  | The item statis |
| description |  ``` Optional ```  | The item description |
| createdSince |  ``` Optional ```  | Filter for item's creation date start range |
| createdUntil |  ``` Optional ```  | Filter for item's creation date end range |



#### Example Usage

```python
subscription_id = 'subscription_id'
page = 61
size = 61
name = 'name'
code = 'code'
status = 'status'
description = 'description'
created_since = 'created_since'
created_until = 'created_until'

result = subscriptions_controller.get_subscription_items(subscription_id, page, size, name, code, status, description, created_since, created_until)

```


### <a name="get_subscription_item"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_subscription_item") get_subscription_item

> Get Subscription Item

```python
def get_subscription_item(self,
                              subscription_id,
                              item_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |
| itemId |  ``` Required ```  | Item id |



#### Example Usage

```python
subscription_id = 'subscription_id'
item_id = 'item_id'

result = subscriptions_controller.get_subscription_item(subscription_id, item_id)

```


### <a name="get_subscriptions"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_subscriptions") get_subscriptions

> Gets all subscriptions

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

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| code |  ``` Optional ```  | Filter for subscription's code |
| billingType |  ``` Optional ```  | Filter for subscription's billing type |
| customerId |  ``` Optional ```  | Filter for subscription's customer id |
| planId |  ``` Optional ```  | Filter for subscription's plan id |
| cardId |  ``` Optional ```  | Filter for subscription's card id |
| status |  ``` Optional ```  | Filter for subscription's status |
| nextBillingSince |  ``` Optional ```  | Filter for subscription's next billing date start range |
| nextBillingUntil |  ``` Optional ```  | Filter for subscription's next billing date end range |
| createdSince |  ``` Optional ```  | Filter for subscription's creation date start range |
| createdUntil |  ``` Optional ```  | Filter for subscriptions creation date end range |



#### Example Usage

```python
page = 61
size = 61
code = 'code'
billing_type = 'billing_type'
customer_id = 'customer_id'
plan_id = 'plan_id'
card_id = 'card_id'
status = 'status'
next_billing_since = datetime.now()
next_billing_until = datetime.now()
created_since = datetime.now()
created_until = datetime.now()

result = subscriptions_controller.get_subscriptions(page, size, code, billing_type, customer_id, plan_id, card_id, status, next_billing_since, next_billing_until, created_since, created_until)

```


### <a name="cancel_subscription"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.cancel_subscription") cancel_subscription

> Cancels a subscription

```python
def cancel_subscription(self,
                            subscription_id,
                            request=None,
                            idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| request |  ``` Optional ```  | Request for cancelling a subscription |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = CreateCancelSubscriptionRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.cancel_subscription(subscription_id, request, idempotency_key)

```


### <a name="create_increment"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.create_increment") create_increment

> Creates a increment

```python
def create_increment(self,
                         subscription_id,
                         request,
                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| request |  ``` Required ```  | Request for creating a increment |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = CreateIncrementRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.create_increment(subscription_id, request, idempotency_key)

```


### <a name="create_usage"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.create_usage") create_usage

> Creates a usage

```python
def create_usage(self,
                     subscription_id,
                     item_id,
                     body,
                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |
| itemId |  ``` Required ```  | Item id |
| body |  ``` Required ```  | Request for creating a usage |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
item_id = 'item_id'
body = CreateUsageRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.create_usage(subscription_id, item_id, body, idempotency_key)

```


### <a name="create_subscription"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.create_subscription") create_subscription

> Creates a new subscription

```python
def create_subscription(self,
                            body,
                            idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | Request for creating a subscription |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = CreateSubscriptionRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.create_subscription(body, idempotency_key)

```


### <a name="get_discount_by_id"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_discount_by_id") get_discount_by_id

> TODO: Add a method description

```python
def get_discount_by_id(self,
                           subscription_id,
                           discount_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| discountId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
discount_id = 'discountId'

result = subscriptions_controller.get_discount_by_id(subscription_id, discount_id)

```


### <a name="update_subscription_affiliation_id"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_affiliation_id") update_subscription_affiliation_id

> TODO: Add a method description

```python
def update_subscription_affiliation_id(self,
                                           subscription_id,
                                           request,
                                           idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | Request for updating a subscription affiliation id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateSubscriptionAffiliationIdRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_affiliation_id(subscription_id, request, idempotency_key)

```


### <a name="update_subscription_metadata"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_metadata") update_subscription_metadata

> Updates the metadata from a subscription

```python
def update_subscription_metadata(self,
                                     subscription_id,
                                     request,
                                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| request |  ``` Required ```  | Request for updating the subscrption metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateMetadataRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_metadata(subscription_id, request, idempotency_key)

```


### <a name="delete_increment"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.delete_increment") delete_increment

> Deletes a increment

```python
def delete_increment(self,
                         subscription_id,
                         increment_id,
                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| incrementId |  ``` Required ```  | Increment id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
increment_id = 'increment_id'
idempotency_key = 'idempotency-key'

result = subscriptions_controller.delete_increment(subscription_id, increment_id, idempotency_key)

```


### <a name="get_subscription_cycles"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_subscription_cycles") get_subscription_cycles

> TODO: Add a method description

```python
def get_subscription_cycles(self,
                                subscription_id,
                                page,
                                size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |
| page |  ``` Required ```  | Page number |
| size |  ``` Required ```  | Page size |



#### Example Usage

```python
subscription_id = 'subscription_id'
page = 'page'
size = 'size'

result = subscriptions_controller.get_subscription_cycles(subscription_id, page, size)

```


### <a name="get_increment_by_id"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_increment_by_id") get_increment_by_id

> TODO: Add a method description

```python
def get_increment_by_id(self,
                            subscription_id,
                            increment_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription Id |
| incrementId |  ``` Required ```  | The increment Id |



#### Example Usage

```python
subscription_id = 'subscription_id'
increment_id = 'increment_id'

result = subscriptions_controller.get_increment_by_id(subscription_id, increment_id)

```


### <a name="get_discounts"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_discounts") get_discounts

> TODO: Add a method description

```python
def get_discounts(self,
                      subscription_id,
                      page,
                      size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| page |  ``` Required ```  | Page number |
| size |  ``` Required ```  | Page size |



#### Example Usage

```python
subscription_id = 'subscription_id'
page = 61
size = 61

result = subscriptions_controller.get_discounts(subscription_id, page, size)

```


### <a name="update_subscription_billing_date"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_billing_date") update_subscription_billing_date

> Updates the billing date from a subscription

```python
def update_subscription_billing_date(self,
                                         subscription_id,
                                         request,
                                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| request |  ``` Required ```  | Request for updating the subscription billing date |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateSubscriptionBillingDateRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_billing_date(subscription_id, request, idempotency_key)

```


### <a name="delete_subscription_item"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.delete_subscription_item") delete_subscription_item

> Deletes a subscription item

```python
def delete_subscription_item(self,
                                 subscription_id,
                                 subscription_item_id,
                                 idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| subscriptionItemId |  ``` Required ```  | Subscription item id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
subscription_item_id = 'subscription_item_id'
idempotency_key = 'idempotency-key'

result = subscriptions_controller.delete_subscription_item(subscription_id, subscription_item_id, idempotency_key)

```


### <a name="get_increments"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_increments") get_increments

> TODO: Add a method description

```python
def get_increments(self,
                       subscription_id,
                       page=None,
                       size=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |



#### Example Usage

```python
subscription_id = 'subscription_id'
page = 61
size = 61

result = subscriptions_controller.get_increments(subscription_id, page, size)

```


### <a name="update_subscription_due_days"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_due_days") update_subscription_due_days

> Updates the boleto due days from a subscription

```python
def update_subscription_due_days(self,
                                     subscription_id,
                                     request,
                                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |
| request |  ``` Required ```  | TODO: Add a parameter description |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateSubscriptionDueDaysRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_due_days(subscription_id, request, idempotency_key)

```


### <a name="update_subscription_start_at"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_start_at") update_subscription_start_at

> Updates the start at date from a subscription

```python
def update_subscription_start_at(self,
                                     subscription_id,
                                     request,
                                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| request |  ``` Required ```  | Request for updating the subscription start date |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateSubscriptionStartAtRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_start_at(subscription_id, request, idempotency_key)

```


### <a name="update_subscription_item"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_item") update_subscription_item

> Updates a subscription item

```python
def update_subscription_item(self,
                                 subscription_id,
                                 item_id,
                                 body,
                                 idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |
| itemId |  ``` Required ```  | Item id |
| body |  ``` Required ```  | Request for updating a subscription item |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
item_id = 'item_id'
body = UpdateSubscriptionItemRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_item(subscription_id, item_id, body, idempotency_key)

```


### <a name="create_subscription_item"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.create_subscription_item") create_subscription_item

> Creates a new Subscription item

```python
def create_subscription_item(self,
                                 subscription_id,
                                 request,
                                 idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |
| request |  ``` Required ```  | Request for creating a subscription item |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = CreateSubscriptionItemRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.create_subscription_item(subscription_id, request, idempotency_key)

```


### <a name="get_subscription"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_subscription") get_subscription

> Gets a subscription

```python
def get_subscription(self,
                         subscription_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription id |



#### Example Usage

```python
subscription_id = 'subscription_id'

result = subscriptions_controller.get_subscription(subscription_id)

```


### <a name="get_usages"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_usages") get_usages

> Lists all usages from a subscription item

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

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| itemId |  ``` Required ```  | The subscription item id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| code |  ``` Optional ```  | Identification code in the client system |
| group |  ``` Optional ```  | Identification group in the client system |
| usedSince |  ``` Optional ```  | TODO: Add a parameter description |
| usedUntil |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
item_id = 'item_id'
page = 61
size = 61
code = 'code'
group = 'group'
used_since = datetime.now()
used_until = datetime.now()

result = subscriptions_controller.get_usages(subscription_id, item_id, page, size, code, group, used_since, used_until)

```


### <a name="update_latest_period_end_at"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_latest_period_end_at") update_latest_period_end_at

> TODO: Add a method description

```python
def update_latest_period_end_at(self,
                                    subscription_id,
                                    request,
                                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | Request for updating the end date of the current signature cycle |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateCurrentCycleEndDateRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_latest_period_end_at(subscription_id, request, idempotency_key)

```


### <a name="update_subscription_minium_price"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.update_subscription_minium_price") update_subscription_minium_price

> Atualização do valor mínimo da assinatura

```python
def update_subscription_minium_price(self,
                                         subscription_id,
                                         request,
                                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |
| request |  ``` Required ```  | Request da requisição com o valor mínimo que será configurado |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
request = UpdateSubscriptionMinimumPriceRequest()
idempotency_key = 'idempotency-key'

result = subscriptions_controller.update_subscription_minium_price(subscription_id, request, idempotency_key)

```


### <a name="get_subscription_cycle_by_id"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_subscription_cycle_by_id") get_subscription_cycle_by_id

> TODO: Add a method description

```python
def get_subscription_cycle_by_id(self,
                                     subscription_id,
                                     cycle_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription id |
| cycleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
cycle_id = 'cycleId'

result = subscriptions_controller.get_subscription_cycle_by_id(subscription_id, cycle_id)

```


### <a name="renew_subscription"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.renew_subscription") renew_subscription

> TODO: Add a method description

```python
def renew_subscription(self,
                           subscription_id,
                           idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | TODO: Add a parameter description |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
idempotency_key = 'idempotency-key'

result = subscriptions_controller.renew_subscription(subscription_id, idempotency_key)

```


### <a name="get_usage_report"></a>![Method: ](https://apidocs.io/img/method.png ".SubscriptionsController.get_usage_report") get_usage_report

> TODO: Add a method description

```python
def get_usage_report(self,
                         subscription_id,
                         period_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | The subscription Id |
| periodId |  ``` Required ```  | The period Id |



#### Example Usage

```python
subscription_id = 'subscription_id'
period_id = 'period_id'

result = subscriptions_controller.get_usage_report(subscription_id, period_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="orders_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OrdersController") OrdersController

### Get controller instance

An instance of the ``` OrdersController ``` class can be accessed from the API Client.

```python
 orders_controller = client.orders
```

### <a name="get_orders"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.get_orders") get_orders

> Gets all orders

```python
def get_orders(self,
                   page=None,
                   size=None,
                   code=None,
                   status=None,
                   created_since=None,
                   created_until=None,
                   customer_id=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| code |  ``` Optional ```  | Filter for order's code |
| status |  ``` Optional ```  | Filter for order's status |
| createdSince |  ``` Optional ```  | Filter for order's creation date start range |
| createdUntil |  ``` Optional ```  | Filter for order's creation date end range |
| customerId |  ``` Optional ```  | Filter for order's customer id |



#### Example Usage

```python
page = 61
size = 61
code = 'code'
status = 'status'
created_since = datetime.now()
created_until = datetime.now()
customer_id = 'customer_id'

result = orders_controller.get_orders(page, size, code, status, created_since, created_until, customer_id)

```


### <a name="delete_all_order_items"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.delete_all_order_items") delete_all_order_items

> TODO: Add a method description

```python
def delete_all_order_items(self,
                               order_id,
                               idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orderId |  ``` Required ```  | Order Id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
order_id = 'orderId'
idempotency_key = 'idempotency-key'

result = orders_controller.delete_all_order_items(order_id, idempotency_key)

```


### <a name="update_order_item"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.update_order_item") update_order_item

> TODO: Add a method description

```python
def update_order_item(self,
                          order_id,
                          item_id,
                          request,
                          idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orderId |  ``` Required ```  | Order Id |
| itemId |  ``` Required ```  | Item Id |
| request |  ``` Required ```  | Item Model |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
order_id = 'orderId'
item_id = 'itemId'
request = UpdateOrderItemRequest()
idempotency_key = 'idempotency-key'

result = orders_controller.update_order_item(order_id, item_id, request, idempotency_key)

```


### <a name="delete_order_item"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.delete_order_item") delete_order_item

> TODO: Add a method description

```python
def delete_order_item(self,
                          order_id,
                          item_id,
                          idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orderId |  ``` Required ```  | Order Id |
| itemId |  ``` Required ```  | Item Id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
order_id = 'orderId'
item_id = 'itemId'
idempotency_key = 'idempotency-key'

result = orders_controller.delete_order_item(order_id, item_id, idempotency_key)

```


### <a name="close_order"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.close_order") close_order

> TODO: Add a method description

```python
def close_order(self,
                    id,
                    request,
                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | Order Id |
| request |  ``` Required ```  | Update Order Model |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 'id'
request = UpdateOrderStatusRequest()
idempotency_key = 'idempotency-key'

result = orders_controller.close_order(id, request, idempotency_key)

```


### <a name="create_order"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.create_order") create_order

> Creates a new Order

```python
def create_order(self,
                     body,
                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | Request for creating an order |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = CreateOrderRequest()
idempotency_key = 'idempotency-key'

result = orders_controller.create_order(body, idempotency_key)

```


### <a name="create_order_item"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.create_order_item") create_order_item

> TODO: Add a method description

```python
def create_order_item(self,
                          order_id,
                          request,
                          idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orderId |  ``` Required ```  | Order Id |
| request |  ``` Required ```  | Order Item Model |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
order_id = 'orderId'
request = CreateOrderItemRequest()
idempotency_key = 'idempotency-key'

result = orders_controller.create_order_item(order_id, request, idempotency_key)

```


### <a name="get_order_item"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.get_order_item") get_order_item

> TODO: Add a method description

```python
def get_order_item(self,
                       order_id,
                       item_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orderId |  ``` Required ```  | Order Id |
| itemId |  ``` Required ```  | Item Id |



#### Example Usage

```python
order_id = 'orderId'
item_id = 'itemId'

result = orders_controller.get_order_item(order_id, item_id)

```


### <a name="update_order_metadata"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.update_order_metadata") update_order_metadata

> Updates the metadata from an order

```python
def update_order_metadata(self,
                              order_id,
                              request,
                              idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orderId |  ``` Required ```  | The order id |
| request |  ``` Required ```  | Request for updating the order metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
order_id = 'order_id'
request = UpdateMetadataRequest()
idempotency_key = 'idempotency-key'

result = orders_controller.update_order_metadata(order_id, request, idempotency_key)

```


### <a name="get_order"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.get_order") get_order

> Gets an order

```python
def get_order(self,
                  order_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| orderId |  ``` Required ```  | Order id |



#### Example Usage

```python
order_id = 'order_id'

result = orders_controller.get_order(order_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="invoices_controller"></a>![Class: ](https://apidocs.io/img/class.png ".InvoicesController") InvoicesController

### Get controller instance

An instance of the ``` InvoicesController ``` class can be accessed from the API Client.

```python
 invoices_controller = client.invoices
```

### <a name="get_partial_invoice"></a>![Method: ](https://apidocs.io/img/method.png ".InvoicesController.get_partial_invoice") get_partial_invoice

> TODO: Add a method description

```python
def get_partial_invoice(self,
                            subscription_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |



#### Example Usage

```python
subscription_id = 'subscription_id'

result = invoices_controller.get_partial_invoice(subscription_id)

```


### <a name="cancel_invoice"></a>![Method: ](https://apidocs.io/img/method.png ".InvoicesController.cancel_invoice") cancel_invoice

> Cancels an invoice

```python
def cancel_invoice(self,
                       invoice_id,
                       idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| invoiceId |  ``` Required ```  | Invoice id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
invoice_id = 'invoice_id'
idempotency_key = 'idempotency-key'

result = invoices_controller.cancel_invoice(invoice_id, idempotency_key)

```


### <a name="create_invoice"></a>![Method: ](https://apidocs.io/img/method.png ".InvoicesController.create_invoice") create_invoice

> Create an Invoice

```python
def create_invoice(self,
                       subscription_id,
                       cycle_id,
                       request=None,
                       idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subscriptionId |  ``` Required ```  | Subscription Id |
| cycleId |  ``` Required ```  | Cycle Id |
| request |  ``` Optional ```  | TODO: Add a parameter description |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
subscription_id = 'subscription_id'
cycle_id = 'cycle_id'
request = CreateInvoiceRequest()
idempotency_key = 'idempotency-key'

result = invoices_controller.create_invoice(subscription_id, cycle_id, request, idempotency_key)

```


### <a name="update_invoice_metadata"></a>![Method: ](https://apidocs.io/img/method.png ".InvoicesController.update_invoice_metadata") update_invoice_metadata

> Updates the metadata from an invoice

```python
def update_invoice_metadata(self,
                                invoice_id,
                                request,
                                idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| invoiceId |  ``` Required ```  | The invoice id |
| request |  ``` Required ```  | Request for updating the invoice metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
invoice_id = 'invoice_id'
request = UpdateMetadataRequest()
idempotency_key = 'idempotency-key'

result = invoices_controller.update_invoice_metadata(invoice_id, request, idempotency_key)

```


### <a name="get_invoices"></a>![Method: ](https://apidocs.io/img/method.png ".InvoicesController.get_invoices") get_invoices

> Gets all invoices

```python
def get_invoices(self,
                     page=None,
                     size=None,
                     code=None,
                     customer_id=None,
                     subscription_id=None,
                     created_since=None,
                     created_until=None,
                     status=None,
                     due_since=None,
                     due_until=None,
                     customer_document=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| code |  ``` Optional ```  | Filter for Invoice's code |
| customerId |  ``` Optional ```  | Filter for Invoice's customer id |
| subscriptionId |  ``` Optional ```  | Filter for Invoice's subscription id |
| createdSince |  ``` Optional ```  | Filter for Invoice's creation date start range |
| createdUntil |  ``` Optional ```  | Filter for Invoices creation date end range |
| status |  ``` Optional ```  | Filter for Invoice's status |
| dueSince |  ``` Optional ```  | Filter for Invoice's due date start range |
| dueUntil |  ``` Optional ```  | Filter for Invoice's due date end range |
| customerDocument |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 152
size = 152
code = 'code'
customer_id = 'customer_id'
subscription_id = 'subscription_id'
created_since = datetime.now()
created_until = datetime.now()
status = 'status'
due_since = datetime.now()
due_until = datetime.now()
customer_document = 'customer_document'

result = invoices_controller.get_invoices(page, size, code, customer_id, subscription_id, created_since, created_until, status, due_since, due_until, customer_document)

```


### <a name="get_invoice"></a>![Method: ](https://apidocs.io/img/method.png ".InvoicesController.get_invoice") get_invoice

> Gets an invoice

```python
def get_invoice(self,
                    invoice_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| invoiceId |  ``` Required ```  | Invoice Id |



#### Example Usage

```python
invoice_id = 'invoice_id'

result = invoices_controller.get_invoice(invoice_id)

```


### <a name="update_invoice_status"></a>![Method: ](https://apidocs.io/img/method.png ".InvoicesController.update_invoice_status") update_invoice_status

> Updates the status from an invoice

```python
def update_invoice_status(self,
                              invoice_id,
                              request,
                              idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| invoiceId |  ``` Required ```  | Invoice Id |
| request |  ``` Required ```  | Request for updating an invoice's status |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
invoice_id = 'invoice_id'
request = UpdateInvoiceStatusRequest()
idempotency_key = 'idempotency-key'

result = invoices_controller.update_invoice_status(invoice_id, request, idempotency_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="customers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CustomersController") CustomersController

### Get controller instance

An instance of the ``` CustomersController ``` class can be accessed from the API Client.

```python
 customers_controller = client.customers
```

### <a name="update_card"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.update_card") update_card

> Updates a card

```python
def update_card(self,
                    customer_id,
                    card_id,
                    request,
                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| cardId |  ``` Required ```  | Card id |
| request |  ``` Required ```  | Request for updating a card |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
card_id = 'card_id'
request = UpdateCardRequest()
idempotency_key = 'idempotency-key'

result = customers_controller.update_card(customer_id, card_id, request, idempotency_key)

```


### <a name="update_address"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.update_address") update_address

> Updates an address

```python
def update_address(self,
                       customer_id,
                       address_id,
                       request,
                       idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| addressId |  ``` Required ```  | Address Id |
| request |  ``` Required ```  | Request for updating an address |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
address_id = 'address_id'
request = UpdateAddressRequest()
idempotency_key = 'idempotency-key'

result = customers_controller.update_address(customer_id, address_id, request, idempotency_key)

```


### <a name="delete_access_token"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.delete_access_token") delete_access_token

> Delete a customer's access token

```python
def delete_access_token(self,
                            customer_id,
                            token_id,
                            idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| tokenId |  ``` Required ```  | Token Id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
token_id = 'token_id'
idempotency_key = 'idempotency-key'

result = customers_controller.delete_access_token(customer_id, token_id, idempotency_key)

```


### <a name="create_access_token"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.create_access_token") create_access_token

> Creates a access token for a customer

```python
def create_access_token(self,
                            customer_id,
                            request,
                            idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| request |  ``` Required ```  | Request for creating a access token |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
request = CreateAccessTokenRequest()
idempotency_key = 'idempotency-key'

result = customers_controller.create_access_token(customer_id, request, idempotency_key)

```


### <a name="create_address"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.create_address") create_address

> Creates a new address for a customer

```python
def create_address(self,
                       customer_id,
                       request,
                       idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| request |  ``` Required ```  | Request for creating an address |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
request = CreateAddressRequest()
idempotency_key = 'idempotency-key'

result = customers_controller.create_address(customer_id, request, idempotency_key)

```


### <a name="create_customer"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.create_customer") create_customer

> Creates a new customer

```python
def create_customer(self,
                        request,
                        idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Request for creating a customer |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = CreateCustomerRequest()
idempotency_key = 'idempotency-key'

result = customers_controller.create_customer(request, idempotency_key)

```


### <a name="delete_access_tokens"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.delete_access_tokens") delete_access_tokens

> Delete a Customer's access tokens

```python
def delete_access_tokens(self,
                             customer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |



#### Example Usage

```python
customer_id = 'customer_id'

result = customers_controller.delete_access_tokens(customer_id)

```


### <a name="get_address"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_address") get_address

> Get a customer's address

```python
def get_address(self,
                    customer_id,
                    address_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer id |
| addressId |  ``` Required ```  | Address Id |



#### Example Usage

```python
customer_id = 'customer_id'
address_id = 'address_id'

result = customers_controller.get_address(customer_id, address_id)

```


### <a name="delete_address"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.delete_address") delete_address

> Delete a Customer's address

```python
def delete_address(self,
                       customer_id,
                       address_id,
                       idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| addressId |  ``` Required ```  | Address Id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
address_id = 'address_id'
idempotency_key = 'idempotency-key'

result = customers_controller.delete_address(customer_id, address_id, idempotency_key)

```


### <a name="create_card"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.create_card") create_card

> Creates a new card for a customer

```python
def create_card(self,
                    customer_id,
                    request,
                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer id |
| request |  ``` Required ```  | Request for creating a card |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
request = CreateCardRequest()
idempotency_key = 'idempotency-key'

result = customers_controller.create_card(customer_id, request, idempotency_key)

```


### <a name="get_customers"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_customers") get_customers

> Get all Customers

```python
def get_customers(self,
                      name=None,
                      document=None,
                      page=1,
                      size=10,
                      email=None,
                      code=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| name |  ``` Optional ```  | Name of the Customer |
| document |  ``` Optional ```  | Document of the Customer |
| page |  ``` Optional ```  ``` DefaultValue ```  | Current page the the search |
| size |  ``` Optional ```  ``` DefaultValue ```  | Quantity pages of the search |
| email |  ``` Optional ```  | Customer's email |
| code |  ``` Optional ```  | Customer's code |



#### Example Usage

```python
name = 'name'
document = 'document'
page = 1
size = 10
email = 'email'
code = 'Code'

result = customers_controller.get_customers(name, document, page, size, email, code)

```


### <a name="update_customer"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.update_customer") update_customer

> Updates a customer

```python
def update_customer(self,
                        customer_id,
                        request,
                        idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer id |
| request |  ``` Required ```  | Request for updating a customer |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
request = UpdateCustomerRequest()
idempotency_key = 'idempotency-key'

result = customers_controller.update_customer(customer_id, request, idempotency_key)

```


### <a name="get_access_tokens"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_access_tokens") get_access_tokens

> Get all access tokens from a customer

```python
def get_access_tokens(self,
                          customer_id,
                          page=None,
                          size=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |



#### Example Usage

```python
customer_id = 'customer_id'
page = 152
size = 152

result = customers_controller.get_access_tokens(customer_id, page, size)

```


### <a name="get_cards"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_cards") get_cards

> Get all cards from a customer

```python
def get_cards(self,
                  customer_id,
                  page=None,
                  size=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |



#### Example Usage

```python
customer_id = 'customer_id'
page = 152
size = 152

result = customers_controller.get_cards(customer_id, page, size)

```


### <a name="renew_card"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.renew_card") renew_card

> Renew a card

```python
def renew_card(self,
                   customer_id,
                   card_id,
                   idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer id |
| cardId |  ``` Required ```  | Card Id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
card_id = 'card_id'
idempotency_key = 'idempotency-key'

result = customers_controller.renew_card(customer_id, card_id, idempotency_key)

```


### <a name="get_access_token"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_access_token") get_access_token

> Get a Customer's access token

```python
def get_access_token(self,
                         customer_id,
                         token_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| tokenId |  ``` Required ```  | Token Id |



#### Example Usage

```python
customer_id = 'customer_id'
token_id = 'token_id'

result = customers_controller.get_access_token(customer_id, token_id)

```


### <a name="update_customer_metadata"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.update_customer_metadata") update_customer_metadata

> Updates the metadata a customer

```python
def update_customer_metadata(self,
                                 customer_id,
                                 request,
                                 idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | The customer id |
| request |  ``` Required ```  | Request for updating the customer metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
request = UpdateMetadataRequest()
idempotency_key = 'idempotency-key'

result = customers_controller.update_customer_metadata(customer_id, request, idempotency_key)

```


### <a name="delete_card"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.delete_card") delete_card

> Delete a customer's card

```python
def delete_card(self,
                    customer_id,
                    card_id,
                    idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |
| cardId |  ``` Required ```  | Card Id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
customer_id = 'customer_id'
card_id = 'card_id'
idempotency_key = 'idempotency-key'

result = customers_controller.delete_card(customer_id, card_id, idempotency_key)

```


### <a name="get_addresses"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_addresses") get_addresses

> Gets all adressess from a customer

```python
def get_addresses(self,
                      customer_id,
                      page=None,
                      size=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |



#### Example Usage

```python
customer_id = 'customer_id'
page = 152
size = 152

result = customers_controller.get_addresses(customer_id, page, size)

```


### <a name="get_customer"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_customer") get_customer

> Get a customer

```python
def get_customer(self,
                     customer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer Id |



#### Example Usage

```python
customer_id = 'customer_id'

result = customers_controller.get_customer(customer_id)

```


### <a name="get_card"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_card") get_card

> Get a customer's card

```python
def get_card(self,
                 customer_id,
                 card_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerId |  ``` Required ```  | Customer id |
| cardId |  ``` Required ```  | Card id |



#### Example Usage

```python
customer_id = 'customer_id'
card_id = 'card_id'

result = customers_controller.get_card(customer_id, card_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="charges_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ChargesController") ChargesController

### Get controller instance

An instance of the ``` ChargesController ``` class can be accessed from the API Client.

```python
 charges_controller = client.charges
```

### <a name="update_charge_metadata"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.update_charge_metadata") update_charge_metadata

> Updates the metadata from a charge

```python
def update_charge_metadata(self,
                               charge_id,
                               request,
                               idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | The charge id |
| request |  ``` Required ```  | Request for updating the charge metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
charge_id = 'charge_id'
request = UpdateMetadataRequest()
idempotency_key = 'idempotency-key'

result = charges_controller.update_charge_metadata(charge_id, request, idempotency_key)

```


### <a name="capture_charge"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.capture_charge") capture_charge

> Captures a charge

```python
def capture_charge(self,
                       charge_id,
                       request=None,
                       idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | Charge id |
| request |  ``` Optional ```  | Request for capturing a charge |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
charge_id = 'charge_id'
request = CreateCaptureChargeRequest()
idempotency_key = 'idempotency-key'

result = charges_controller.capture_charge(charge_id, request, idempotency_key)

```


### <a name="update_charge_payment_method"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.update_charge_payment_method") update_charge_payment_method

> Updates a charge's payment method

```python
def update_charge_payment_method(self,
                                     charge_id,
                                     request,
                                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | Charge id |
| request |  ``` Required ```  | Request for updating the payment method from a charge |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
charge_id = 'charge_id'
request = UpdateChargePaymentMethodRequest()
idempotency_key = 'idempotency-key'

result = charges_controller.update_charge_payment_method(charge_id, request, idempotency_key)

```


### <a name="get_charge_transactions"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.get_charge_transactions") get_charge_transactions

> TODO: Add a method description

```python
def get_charge_transactions(self,
                                charge_id,
                                page=None,
                                size=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | Charge Id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |



#### Example Usage

```python
charge_id = 'charge_id'
page = 152
size = 152

result = charges_controller.get_charge_transactions(charge_id, page, size)

```


### <a name="update_charge_due_date"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.update_charge_due_date") update_charge_due_date

> Updates the due date from a charge

```python
def update_charge_due_date(self,
                               charge_id,
                               request,
                               idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | Charge Id |
| request |  ``` Required ```  | Request for updating the due date |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
charge_id = 'charge_id'
request = UpdateChargeDueDateRequest()
idempotency_key = 'idempotency-key'

result = charges_controller.update_charge_due_date(charge_id, request, idempotency_key)

```


### <a name="get_charges"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.get_charges") get_charges

> Lists all charges

```python
def get_charges(self,
                    page=None,
                    size=None,
                    code=None,
                    status=None,
                    payment_method=None,
                    customer_id=None,
                    order_id=None,
                    created_since=None,
                    created_until=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| code |  ``` Optional ```  | Filter for charge's code |
| status |  ``` Optional ```  | Filter for charge's status |
| paymentMethod |  ``` Optional ```  | Filter for charge's payment method |
| customerId |  ``` Optional ```  | Filter for charge's customer id |
| orderId |  ``` Optional ```  | Filter for charge's order id |
| createdSince |  ``` Optional ```  | Filter for the beginning of the range for charge's creation |
| createdUntil |  ``` Optional ```  | Filter for the end of the range for charge's creation |



#### Example Usage

```python
page = 152
size = 152
code = 'code'
status = 'status'
payment_method = 'payment_method'
customer_id = 'customer_id'
order_id = 'order_id'
created_since = datetime.now()
created_until = datetime.now()

result = charges_controller.get_charges(page, size, code, status, payment_method, customer_id, order_id, created_since, created_until)

```


### <a name="update_charge_card"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.update_charge_card") update_charge_card

> Updates the card from a charge

```python
def update_charge_card(self,
                           charge_id,
                           request,
                           idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | Charge id |
| request |  ``` Required ```  | Request for updating a charge's card |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
charge_id = 'charge_id'
request = UpdateChargeCardRequest()
idempotency_key = 'idempotency-key'

result = charges_controller.update_charge_card(charge_id, request, idempotency_key)

```


### <a name="get_charge"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.get_charge") get_charge

> Get a charge from its id

```python
def get_charge(self,
                   charge_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | Charge id |



#### Example Usage

```python
charge_id = 'charge_id'

result = charges_controller.get_charge(charge_id)

```


### <a name="get_charges_summary"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.get_charges_summary") get_charges_summary

> TODO: Add a method description

```python
def get_charges_summary(self,
                            status,
                            created_since=None,
                            created_until=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| status |  ``` Required ```  | TODO: Add a parameter description |
| createdSince |  ``` Optional ```  | TODO: Add a parameter description |
| createdUntil |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
status = 'status'
created_since = datetime.now()
created_until = datetime.now()

result = charges_controller.get_charges_summary(status, created_since, created_until)

```


### <a name="retry_charge"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.retry_charge") retry_charge

> Retries a charge

```python
def retry_charge(self,
                     charge_id,
                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | Charge id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
charge_id = 'charge_id'
idempotency_key = 'idempotency-key'

result = charges_controller.retry_charge(charge_id, idempotency_key)

```


### <a name="cancel_charge"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.cancel_charge") cancel_charge

> Cancel a charge

```python
def cancel_charge(self,
                      charge_id,
                      request=None,
                      idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | Charge id |
| request |  ``` Optional ```  | Request for cancelling a charge |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
charge_id = 'charge_id'
request = CreateCancelChargeRequest()
idempotency_key = 'idempotency-key'

result = charges_controller.cancel_charge(charge_id, request, idempotency_key)

```


### <a name="create_charge"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.create_charge") create_charge

> Creates a new charge

```python
def create_charge(self,
                      request,
                      idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Request for creating a charge |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = CreateChargeRequest()
idempotency_key = 'idempotency-key'

result = charges_controller.create_charge(request, idempotency_key)

```


### <a name="confirm_payment"></a>![Method: ](https://apidocs.io/img/method.png ".ChargesController.confirm_payment") confirm_payment

> TODO: Add a method description

```python
def confirm_payment(self,
                        charge_id,
                        request=None,
                        idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| chargeId |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Optional ```  | Request for confirm payment |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
charge_id = 'charge_id'
request = CreateConfirmPaymentRequest()
idempotency_key = 'idempotency-key'

result = charges_controller.confirm_payment(charge_id, request, idempotency_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="transfers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TransfersController") TransfersController

### Get controller instance

An instance of the ``` TransfersController ``` class can be accessed from the API Client.

```python
 transfers_controller = client.transfers
```

### <a name="get_transfer_by_id"></a>![Method: ](https://apidocs.io/img/method.png ".TransfersController.get_transfer_by_id") get_transfer_by_id

> TODO: Add a method description

```python
def get_transfer_by_id(self,
                           transfer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| transferId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
transfer_id = 'transfer_id'

result = transfers_controller.get_transfer_by_id(transfer_id)

```


### <a name="create_transfer"></a>![Method: ](https://apidocs.io/img/method.png ".TransfersController.create_transfer") create_transfer

> TODO: Add a method description

```python
def create_transfer(self,
                        request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = CreateTransfer()

result = transfers_controller.create_transfer(request)

```


### <a name="get_transfers"></a>![Method: ](https://apidocs.io/img/method.png ".TransfersController.get_transfers") get_transfers

> Gets all transfers

```python
def get_transfers(self)
```

#### Example Usage

```python

result = transfers_controller.get_transfers()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="recipients_controller"></a>![Class: ](https://apidocs.io/img/class.png ".RecipientsController") RecipientsController

### Get controller instance

An instance of the ``` RecipientsController ``` class can be accessed from the API Client.

```python
 recipients_controller = client.recipients
```

### <a name="get_transfer"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_transfer") get_transfer

> Gets a transfer

```python
def get_transfer(self,
                     recipient_id,
                     transfer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| transferId |  ``` Required ```  | Transfer id |



#### Example Usage

```python
recipient_id = 'recipient_id'
transfer_id = 'transfer_id'

result = recipients_controller.get_transfer(recipient_id, transfer_id)

```


### <a name="update_recipient"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.update_recipient") update_recipient

> Updates a recipient

```python
def update_recipient(self,
                         recipient_id,
                         request,
                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| request |  ``` Required ```  | Recipient data |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
request = UpdateRecipientRequest()
idempotency_key = 'idempotency-key'

result = recipients_controller.update_recipient(recipient_id, request, idempotency_key)

```


### <a name="create_anticipation"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.create_anticipation") create_anticipation

> Creates an anticipation

```python
def create_anticipation(self,
                            recipient_id,
                            request,
                            idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| request |  ``` Required ```  | Anticipation data |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
request = CreateAnticipationRequest()
idempotency_key = 'idempotency-key'

result = recipients_controller.create_anticipation(recipient_id, request, idempotency_key)

```


### <a name="get_anticipation_limits"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_anticipation_limits") get_anticipation_limits

> Gets the anticipation limits for a recipient

```python
def get_anticipation_limits(self,
                                recipient_id,
                                timeframe,
                                payment_date)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| timeframe |  ``` Required ```  | Timeframe |
| paymentDate |  ``` Required ```  | Anticipation payment date |



#### Example Usage

```python
recipient_id = 'recipient_id'
timeframe = 'timeframe'
payment_date = datetime.now()

result = recipients_controller.get_anticipation_limits(recipient_id, timeframe, payment_date)

```


### <a name="get_recipients"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_recipients") get_recipients

> Retrieves paginated recipients information

```python
def get_recipients(self,
                       page=None,
                       size=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |



#### Example Usage

```python
page = 111
size = 111

result = recipients_controller.get_recipients(page, size)

```


### <a name="get_withdraw_by_id"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_withdraw_by_id") get_withdraw_by_id

> TODO: Add a method description

```python
def get_withdraw_by_id(self,
                           recipient_id,
                           withdrawal_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | TODO: Add a parameter description |
| withdrawalId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
withdrawal_id = 'withdrawal_id'

result = recipients_controller.get_withdraw_by_id(recipient_id, withdrawal_id)

```


### <a name="update_recipient_default_bank_account"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.update_recipient_default_bank_account") update_recipient_default_bank_account

> Updates the default bank account from a recipient

```python
def update_recipient_default_bank_account(self,
                                              recipient_id,
                                              request,
                                              idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| request |  ``` Required ```  | Bank account data |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
request = UpdateRecipientBankAccountRequest()
idempotency_key = 'idempotency-key'

result = recipients_controller.update_recipient_default_bank_account(recipient_id, request, idempotency_key)

```


### <a name="update_recipient_metadata"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.update_recipient_metadata") update_recipient_metadata

> Updates recipient metadata

```python
def update_recipient_metadata(self,
                                  recipient_id,
                                  request,
                                  idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| request |  ``` Required ```  | Metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
request = UpdateMetadataRequest()
idempotency_key = 'idempotency-key'

result = recipients_controller.update_recipient_metadata(recipient_id, request, idempotency_key)

```


### <a name="get_transfers"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_transfers") get_transfers

> Gets a paginated list of transfers for the recipient

```python
def get_transfers(self,
                      recipient_id,
                      page=None,
                      size=None,
                      status=None,
                      created_since=None,
                      created_until=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| status |  ``` Optional ```  | Filter for transfer status |
| createdSince |  ``` Optional ```  | Filter for start range of transfer creation date |
| createdUntil |  ``` Optional ```  | Filter for end range of transfer creation date |



#### Example Usage

```python
recipient_id = 'recipient_id'
page = 111
size = 111
status = 'status'
created_since = datetime.now()
created_until = datetime.now()

result = recipients_controller.get_transfers(recipient_id, page, size, status, created_since, created_until)

```


### <a name="create_withdraw"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.create_withdraw") create_withdraw

> TODO: Add a method description

```python
def create_withdraw(self,
                        recipient_id,
                        request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
request = CreateWithdrawRequest()

result = recipients_controller.create_withdraw(recipient_id, request)

```


### <a name="update_automatic_anticipation_settings"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.update_automatic_anticipation_settings") update_automatic_anticipation_settings

> Updates recipient metadata

```python
def update_automatic_anticipation_settings(self,
                                               recipient_id,
                                               request,
                                               idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| request |  ``` Required ```  | Metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
request = UpdateAutomaticAnticipationSettingsRequest()
idempotency_key = 'idempotency-key'

result = recipients_controller.update_automatic_anticipation_settings(recipient_id, request, idempotency_key)

```


### <a name="get_anticipation"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_anticipation") get_anticipation

> Gets an anticipation

```python
def get_anticipation(self,
                         recipient_id,
                         anticipation_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| anticipationId |  ``` Required ```  | Anticipation id |



#### Example Usage

```python
recipient_id = 'recipient_id'
anticipation_id = 'anticipation_id'

result = recipients_controller.get_anticipation(recipient_id, anticipation_id)

```


### <a name="update_recipient_transfer_settings"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.update_recipient_transfer_settings") update_recipient_transfer_settings

> TODO: Add a method description

```python
def update_recipient_transfer_settings(self,
                                           recipient_id,
                                           request,
                                           idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient Identificator |
| request |  ``` Required ```  | TODO: Add a parameter description |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
request = UpdateTransferSettingsRequest()
idempotency_key = 'idempotency-key'

result = recipients_controller.update_recipient_transfer_settings(recipient_id, request, idempotency_key)

```


### <a name="get_anticipations"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_anticipations") get_anticipations

> Retrieves a paginated list of anticipations from a recipient

```python
def get_anticipations(self,
                          recipient_id,
                          page=None,
                          size=None,
                          status=None,
                          timeframe=None,
                          payment_date_since=None,
                          payment_date_until=None,
                          created_since=None,
                          created_until=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| status |  ``` Optional ```  | Filter for anticipation status |
| timeframe |  ``` Optional ```  | Filter for anticipation timeframe |
| paymentDateSince |  ``` Optional ```  | Filter for start range for anticipation payment date |
| paymentDateUntil |  ``` Optional ```  | Filter for end range for anticipation payment date |
| createdSince |  ``` Optional ```  | Filter for start range for anticipation creation date |
| createdUntil |  ``` Optional ```  | Filter for end range for anticipation creation date |



#### Example Usage

```python
recipient_id = 'recipient_id'
page = 111
size = 111
status = 'status'
timeframe = 'timeframe'
payment_date_since = datetime.now()
payment_date_until = datetime.now()
created_since = datetime.now()
created_until = datetime.now()

result = recipients_controller.get_anticipations(recipient_id, page, size, status, timeframe, payment_date_since, payment_date_until, created_since, created_until)

```


### <a name="get_recipient"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_recipient") get_recipient

> Retrieves recipient information

```python
def get_recipient(self,
                      recipient_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipiend id |



#### Example Usage

```python
recipient_id = 'recipient_id'

result = recipients_controller.get_recipient(recipient_id)

```


### <a name="get_withdrawals"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_withdrawals") get_withdrawals

> Gets a paginated list of transfers for the recipient

```python
def get_withdrawals(self,
                        recipient_id,
                        page=None,
                        size=None,
                        status=None,
                        created_since=None,
                        created_until=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | TODO: Add a parameter description |
| page |  ``` Optional ```  | TODO: Add a parameter description |
| size |  ``` Optional ```  | TODO: Add a parameter description |
| status |  ``` Optional ```  | TODO: Add a parameter description |
| createdSince |  ``` Optional ```  | TODO: Add a parameter description |
| createdUntil |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
page = 111
size = 111
status = 'status'
created_since = datetime.now()
created_until = datetime.now()

result = recipients_controller.get_withdrawals(recipient_id, page, size, status, created_since, created_until)

```


### <a name="get_balance"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_balance") get_balance

> Get balance information for a recipient

```python
def get_balance(self,
                    recipient_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient id |



#### Example Usage

```python
recipient_id = 'recipient_id'

result = recipients_controller.get_balance(recipient_id)

```


### <a name="create_transfer"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.create_transfer") create_transfer

> Creates a transfer for a recipient

```python
def create_transfer(self,
                        recipient_id,
                        request,
                        idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recipientId |  ``` Required ```  | Recipient Id |
| request |  ``` Required ```  | Transfer data |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
recipient_id = 'recipient_id'
request = CreateTransferRequest()
idempotency_key = 'idempotency-key'

result = recipients_controller.create_transfer(recipient_id, request, idempotency_key)

```


### <a name="create_recipient"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.create_recipient") create_recipient

> Creates a new recipient

```python
def create_recipient(self,
                         request,
                         idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Recipient data |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = CreateRecipientRequest()
idempotency_key = 'idempotency-key'

result = recipients_controller.create_recipient(request, idempotency_key)

```


### <a name="get_recipient_by_code"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_recipient_by_code") get_recipient_by_code

> Retrieves recipient information

```python
def get_recipient_by_code(self,
                              code)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| code |  ``` Required ```  | Recipient code |



#### Example Usage

```python
code = 'code'

result = recipients_controller.get_recipient_by_code(code)

```


### <a name="get_default_recipient"></a>![Method: ](https://apidocs.io/img/method.png ".RecipientsController.get_default_recipient") get_default_recipient

> TODO: Add a method description

```python
def get_default_recipient(self)
```

#### Example Usage

```python

result = recipients_controller.get_default_recipient()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="tokens_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TokensController") TokensController

### Get controller instance

An instance of the ``` TokensController ``` class can be accessed from the API Client.

```python
 tokens_controller = client.tokens
```

### <a name="create_token"></a>![Method: ](https://apidocs.io/img/method.png ".TokensController.create_token") create_token

> *Tags:*  ``` Skips Authentication ``` 

> TODO: Add a method description

```python
def create_token(self,
                     public_key,
                     request,
                     idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| publicKey |  ``` Required ```  | Public key |
| request |  ``` Required ```  | Request for creating a token |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
public_key = 'public_key'
request = CreateTokenRequest()
idempotency_key = 'idempotency-key'

result = tokens_controller.create_token(public_key, request, idempotency_key)

```


### <a name="get_token"></a>![Method: ](https://apidocs.io/img/method.png ".TokensController.get_token") get_token

> *Tags:*  ``` Skips Authentication ``` 

> Gets a token from its id

```python
def get_token(self,
                  id,
                  public_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | Token id |
| publicKey |  ``` Required ```  | Public key |



#### Example Usage

```python
id = 'id'
public_key = 'public_key'

result = tokens_controller.get_token(id, public_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sellers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SellersController") SellersController

### Get controller instance

An instance of the ``` SellersController ``` class can be accessed from the API Client.

```python
 sellers_controller = client.sellers
```

### <a name="create_seller"></a>![Method: ](https://apidocs.io/img/method.png ".SellersController.create_seller") create_seller

> TODO: Add a method description

```python
def create_seller(self,
                      request,
                      idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Seller Model |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
request = CreateSellerRequest()
idempotency_key = 'idempotency-key'

result = sellers_controller.create_seller(request, idempotency_key)

```


### <a name="update_seller_metadata"></a>![Method: ](https://apidocs.io/img/method.png ".SellersController.update_seller_metadata") update_seller_metadata

> TODO: Add a method description

```python
def update_seller_metadata(self,
                               seller_id,
                               request,
                               idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| sellerId |  ``` Required ```  | Seller Id |
| request |  ``` Required ```  | Request for updating the charge metadata |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
seller_id = 'seller_id'
request = UpdateMetadataRequest()
idempotency_key = 'idempotency-key'

result = sellers_controller.update_seller_metadata(seller_id, request, idempotency_key)

```


### <a name="update_seller"></a>![Method: ](https://apidocs.io/img/method.png ".SellersController.update_seller") update_seller

> TODO: Add a method description

```python
def update_seller(self,
                      id,
                      request,
                      idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | Update Seller model |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 'id'
request = UpdateSellerRequest()
idempotency_key = 'idempotency-key'

result = sellers_controller.update_seller(id, request, idempotency_key)

```


### <a name="delete_seller"></a>![Method: ](https://apidocs.io/img/method.png ".SellersController.delete_seller") delete_seller

> TODO: Add a method description

```python
def delete_seller(self,
                      seller_id,
                      idempotency_key=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| sellerId |  ``` Required ```  | Seller Id |
| idempotencyKey |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
seller_id = 'sellerId'
idempotency_key = 'idempotency-key'

result = sellers_controller.delete_seller(seller_id, idempotency_key)

```


### <a name="get_seller_by_id"></a>![Method: ](https://apidocs.io/img/method.png ".SellersController.get_seller_by_id") get_seller_by_id

> TODO: Add a method description

```python
def get_seller_by_id(self,
                         id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | Seller Id |



#### Example Usage

```python
id = 'id'

result = sellers_controller.get_seller_by_id(id)

```


### <a name="get_sellers"></a>![Method: ](https://apidocs.io/img/method.png ".SellersController.get_sellers") get_sellers

> TODO: Add a method description

```python
def get_sellers(self,
                    page=None,
                    size=None,
                    name=None,
                    document=None,
                    code=None,
                    status=None,
                    mtype=None,
                    created_since=None,
                    created_until=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page number |
| size |  ``` Optional ```  | Page size |
| name |  ``` Optional ```  | TODO: Add a parameter description |
| document |  ``` Optional ```  | TODO: Add a parameter description |
| code |  ``` Optional ```  | TODO: Add a parameter description |
| status |  ``` Optional ```  | TODO: Add a parameter description |
| mtype |  ``` Optional ```  | TODO: Add a parameter description |
| createdSince |  ``` Optional ```  | TODO: Add a parameter description |
| createdUntil |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 111
size = 111
name = 'name'
document = 'document'
code = 'code'
status = 'status'
mtype = 'type'
created_since = datetime.now()
created_until = datetime.now()

result = sellers_controller.get_sellers(page, size, name, document, code, status, mtype, created_since, created_until)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="transactions_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TransactionsController") TransactionsController

### Get controller instance

An instance of the ``` TransactionsController ``` class can be accessed from the API Client.

```python
 transactions_controller = client.transactions
```

### <a name="get_transaction"></a>![Method: ](https://apidocs.io/img/method.png ".TransactionsController.get_transaction") get_transaction

> TODO: Add a method description

```python
def get_transaction(self,
                        transaction_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| transactionId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
transaction_id = 'transaction_id'

result = transactions_controller.get_transaction(transaction_id)

```


[Back to List of Controllers](#list_of_controllers)



