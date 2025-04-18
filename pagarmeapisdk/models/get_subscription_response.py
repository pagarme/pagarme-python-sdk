# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_card_response import GetCardResponse
from pagarmeapisdk.models.get_customer_response import GetCustomerResponse
from pagarmeapisdk.models.get_setup_response import GetSetupResponse
from pagarmeapisdk.models.get_subscription_boleto_response import GetSubscriptionBoletoResponse
from pagarmeapisdk.models.get_subscription_split_response import GetSubscriptionSplitResponse


class GetSubscriptionResponse(object):

    """Implementation of the 'GetSubscriptionResponse' model.

    Attributes:
        id (str): The model property of type str.
        code (str): The model property of type str.
        start_at (datetime): The model property of type datetime.
        interval (str): The model property of type str.
        interval_count (int): The model property of type int.
        billing_type (str): The model property of type str.
        current_cycle (GetPeriodResponse): The model property of type
            GetPeriodResponse.
        payment_method (str): The model property of type str.
        currency (str): The model property of type str.
        installments (int): The model property of type int.
        status (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        customer (GetCustomerResponse): The model property of type
            GetCustomerResponse.
        card (GetCardResponse): The model property of type GetCardResponse.
        items (List[GetSubscriptionItemResponse]): The model property of type
            List[GetSubscriptionItemResponse].
        statement_descriptor (str): The model property of type str.
        metadata (Dict[str, str]): The model property of type Dict[str, str].
        setup (GetSetupResponse): The model property of type GetSetupResponse.
        gateway_affiliation_id (str): Affiliation Code
        next_billing_at (datetime): The model property of type datetime.
        billing_day (int): The model property of type int.
        minimum_price (int): The model property of type int.
        canceled_at (datetime): The model property of type datetime.
        discounts (List[GetDiscountResponse]): Subscription discounts
        increments (List[GetIncrementResponse]): Subscription increments
        boleto_due_days (int): Days until boleto expires
        split (GetSubscriptionSplitResponse): Subscription's split response
        boleto (GetSubscriptionBoletoResponse): The model property of type
            GetSubscriptionBoletoResponse.
        manual_billing (bool): The model property of type bool.
        indirect_acceptor (str): Business model identifier

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "code": 'code',
        "start_at": 'start_at',
        "interval": 'interval',
        "interval_count": 'interval_count',
        "billing_type": 'billing_type',
        "current_cycle": 'current_cycle',
        "payment_method": 'payment_method',
        "currency": 'currency',
        "installments": 'installments',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "customer": 'customer',
        "card": 'card',
        "items": 'items',
        "statement_descriptor": 'statement_descriptor',
        "metadata": 'metadata',
        "setup": 'setup',
        "gateway_affiliation_id": 'gateway_affiliation_id',
        "next_billing_at": 'next_billing_at',
        "billing_day": 'billing_day',
        "minimum_price": 'minimum_price',
        "canceled_at": 'canceled_at',
        "discounts": 'discounts',
        "increments": 'increments',
        "boleto_due_days": 'boleto_due_days',
        "split": 'split',
        "boleto": 'boleto',
        "manual_billing": 'manual_billing',
        "indirect_acceptor": 'indirect_acceptor'
    }

    _optionals = [
        'id',
        'code',
        'start_at',
        'interval',
        'interval_count',
        'billing_type',
        'current_cycle',
        'payment_method',
        'currency',
        'installments',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'card',
        'items',
        'statement_descriptor',
        'metadata',
        'setup',
        'gateway_affiliation_id',
        'next_billing_at',
        'billing_day',
        'minimum_price',
        'canceled_at',
        'discounts',
        'increments',
        'boleto_due_days',
        'split',
        'boleto',
        'manual_billing',
        'indirect_acceptor',
    ]

    _nullables = [
        'id',
        'code',
        'start_at',
        'interval',
        'interval_count',
        'billing_type',
        'current_cycle',
        'payment_method',
        'currency',
        'installments',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'card',
        'items',
        'statement_descriptor',
        'metadata',
        'setup',
        'gateway_affiliation_id',
        'next_billing_at',
        'billing_day',
        'minimum_price',
        'canceled_at',
        'discounts',
        'increments',
        'boleto_due_days',
        'split',
        'boleto',
        'manual_billing',
        'indirect_acceptor',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 start_at=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_count=APIHelper.SKIP,
                 billing_type=APIHelper.SKIP,
                 current_cycle=APIHelper.SKIP,
                 payment_method=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 installments=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 card=APIHelper.SKIP,
                 items=APIHelper.SKIP,
                 statement_descriptor=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 setup=APIHelper.SKIP,
                 gateway_affiliation_id=APIHelper.SKIP,
                 next_billing_at=APIHelper.SKIP,
                 billing_day=APIHelper.SKIP,
                 minimum_price=APIHelper.SKIP,
                 canceled_at=APIHelper.SKIP,
                 discounts=APIHelper.SKIP,
                 increments=APIHelper.SKIP,
                 boleto_due_days=APIHelper.SKIP,
                 split=APIHelper.SKIP,
                 boleto=APIHelper.SKIP,
                 manual_billing=APIHelper.SKIP,
                 indirect_acceptor=APIHelper.SKIP):
        """Constructor for the GetSubscriptionResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if code is not APIHelper.SKIP:
            self.code = code 
        if start_at is not APIHelper.SKIP:
            self.start_at = APIHelper.apply_datetime_converter(start_at, APIHelper.RFC3339DateTime) if start_at else None 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_count is not APIHelper.SKIP:
            self.interval_count = interval_count 
        if billing_type is not APIHelper.SKIP:
            self.billing_type = billing_type 
        if current_cycle is not APIHelper.SKIP:
            self.current_cycle = current_cycle 
        if payment_method is not APIHelper.SKIP:
            self.payment_method = payment_method 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if installments is not APIHelper.SKIP:
            self.installments = installments 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if card is not APIHelper.SKIP:
            self.card = card 
        if items is not APIHelper.SKIP:
            self.items = items 
        if statement_descriptor is not APIHelper.SKIP:
            self.statement_descriptor = statement_descriptor 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if setup is not APIHelper.SKIP:
            self.setup = setup 
        if gateway_affiliation_id is not APIHelper.SKIP:
            self.gateway_affiliation_id = gateway_affiliation_id 
        if next_billing_at is not APIHelper.SKIP:
            self.next_billing_at = APIHelper.apply_datetime_converter(next_billing_at, APIHelper.RFC3339DateTime) if next_billing_at else None 
        if billing_day is not APIHelper.SKIP:
            self.billing_day = billing_day 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
        if canceled_at is not APIHelper.SKIP:
            self.canceled_at = APIHelper.apply_datetime_converter(canceled_at, APIHelper.RFC3339DateTime) if canceled_at else None 
        if discounts is not APIHelper.SKIP:
            self.discounts = discounts 
        if increments is not APIHelper.SKIP:
            self.increments = increments 
        if boleto_due_days is not APIHelper.SKIP:
            self.boleto_due_days = boleto_due_days 
        if split is not APIHelper.SKIP:
            self.split = split 
        if boleto is not APIHelper.SKIP:
            self.boleto = boleto 
        if manual_billing is not APIHelper.SKIP:
            self.manual_billing = manual_billing 
        if indirect_acceptor is not APIHelper.SKIP:
            self.indirect_acceptor = indirect_acceptor 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        from pagarmeapisdk.models.get_period_response import GetPeriodResponse
        from pagarmeapisdk.models.get_subscription_item_response import GetSubscriptionItemResponse
        from pagarmeapisdk.models.get_discount_response import GetDiscountResponse
        from pagarmeapisdk.models.get_increment_response import GetIncrementResponse

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        code = dictionary.get("code") if "code" in dictionary.keys() else APIHelper.SKIP
        if 'start_at' in dictionary.keys():
            start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else None
        else:
            start_at = APIHelper.SKIP
        interval = dictionary.get("interval") if "interval" in dictionary.keys() else APIHelper.SKIP
        interval_count = dictionary.get("interval_count") if "interval_count" in dictionary.keys() else APIHelper.SKIP
        billing_type = dictionary.get("billing_type") if "billing_type" in dictionary.keys() else APIHelper.SKIP
        if 'current_cycle' in dictionary.keys():
            current_cycle = GetPeriodResponse.from_dictionary(dictionary.get('current_cycle')) if dictionary.get('current_cycle') else None
        else:
            current_cycle = APIHelper.SKIP
        payment_method = dictionary.get("payment_method") if "payment_method" in dictionary.keys() else APIHelper.SKIP
        currency = dictionary.get("currency") if "currency" in dictionary.keys() else APIHelper.SKIP
        installments = dictionary.get("installments") if "installments" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'customer' in dictionary.keys():
            customer = GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        else:
            customer = APIHelper.SKIP
        if 'card' in dictionary.keys():
            card = GetCardResponse.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        else:
            card = APIHelper.SKIP
        if 'items' in dictionary.keys():
            items = [GetSubscriptionItemResponse.from_dictionary(x) for x in dictionary.get('items')] if dictionary.get('items') else None
        else:
            items = APIHelper.SKIP
        statement_descriptor = dictionary.get("statement_descriptor") if "statement_descriptor" in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        if 'setup' in dictionary.keys():
            setup = GetSetupResponse.from_dictionary(dictionary.get('setup')) if dictionary.get('setup') else None
        else:
            setup = APIHelper.SKIP
        gateway_affiliation_id = dictionary.get("gateway_affiliation_id") if "gateway_affiliation_id" in dictionary.keys() else APIHelper.SKIP
        if 'next_billing_at' in dictionary.keys():
            next_billing_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_billing_at")).datetime if dictionary.get("next_billing_at") else None
        else:
            next_billing_at = APIHelper.SKIP
        billing_day = dictionary.get("billing_day") if "billing_day" in dictionary.keys() else APIHelper.SKIP
        minimum_price = dictionary.get("minimum_price") if "minimum_price" in dictionary.keys() else APIHelper.SKIP
        if 'canceled_at' in dictionary.keys():
            canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else None
        else:
            canceled_at = APIHelper.SKIP
        if 'discounts' in dictionary.keys():
            discounts = [GetDiscountResponse.from_dictionary(x) for x in dictionary.get('discounts')] if dictionary.get('discounts') else None
        else:
            discounts = APIHelper.SKIP
        if 'increments' in dictionary.keys():
            increments = [GetIncrementResponse.from_dictionary(x) for x in dictionary.get('increments')] if dictionary.get('increments') else None
        else:
            increments = APIHelper.SKIP
        boleto_due_days = dictionary.get("boleto_due_days") if "boleto_due_days" in dictionary.keys() else APIHelper.SKIP
        if 'split' in dictionary.keys():
            split = GetSubscriptionSplitResponse.from_dictionary(dictionary.get('split')) if dictionary.get('split') else None
        else:
            split = APIHelper.SKIP
        if 'boleto' in dictionary.keys():
            boleto = GetSubscriptionBoletoResponse.from_dictionary(dictionary.get('boleto')) if dictionary.get('boleto') else None
        else:
            boleto = APIHelper.SKIP
        manual_billing = dictionary.get("manual_billing") if "manual_billing" in dictionary.keys() else APIHelper.SKIP
        indirect_acceptor = dictionary.get("indirect_acceptor") if "indirect_acceptor" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   code,
                   start_at,
                   interval,
                   interval_count,
                   billing_type,
                   current_cycle,
                   payment_method,
                   currency,
                   installments,
                   status,
                   created_at,
                   updated_at,
                   customer,
                   card,
                   items,
                   statement_descriptor,
                   metadata,
                   setup,
                   gateway_affiliation_id,
                   next_billing_at,
                   billing_day,
                   minimum_price,
                   canceled_at,
                   discounts,
                   increments,
                   boleto_due_days,
                   split,
                   boleto,
                   manual_billing,
                   indirect_acceptor)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'start_at={(self.start_at if hasattr(self, "start_at") else None)!r}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!r}, '
                f'interval_count={(self.interval_count if hasattr(self, "interval_count") else None)!r}, '
                f'billing_type={(self.billing_type if hasattr(self, "billing_type") else None)!r}, '
                f'current_cycle={(self.current_cycle if hasattr(self, "current_cycle") else None)!r}, '
                f'payment_method={(self.payment_method if hasattr(self, "payment_method") else None)!r}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!r}, '
                f'installments={(self.installments if hasattr(self, "installments") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'customer={(self.customer if hasattr(self, "customer") else None)!r}, '
                f'card={(self.card if hasattr(self, "card") else None)!r}, '
                f'items={(self.items if hasattr(self, "items") else None)!r}, '
                f'statement_descriptor={(self.statement_descriptor if hasattr(self, "statement_descriptor") else None)!r}, '
                f'metadata={(self.metadata if hasattr(self, "metadata") else None)!r}, '
                f'setup={(self.setup if hasattr(self, "setup") else None)!r}, '
                f'gateway_affiliation_id={(self.gateway_affiliation_id if hasattr(self, "gateway_affiliation_id") else None)!r}, '
                f'next_billing_at={(self.next_billing_at if hasattr(self, "next_billing_at") else None)!r}, '
                f'billing_day={(self.billing_day if hasattr(self, "billing_day") else None)!r}, '
                f'minimum_price={(self.minimum_price if hasattr(self, "minimum_price") else None)!r}, '
                f'canceled_at={(self.canceled_at if hasattr(self, "canceled_at") else None)!r}, '
                f'discounts={(self.discounts if hasattr(self, "discounts") else None)!r}, '
                f'increments={(self.increments if hasattr(self, "increments") else None)!r}, '
                f'boleto_due_days={(self.boleto_due_days if hasattr(self, "boleto_due_days") else None)!r}, '
                f'split={(self.split if hasattr(self, "split") else None)!r}, '
                f'boleto={(self.boleto if hasattr(self, "boleto") else None)!r}, '
                f'manual_billing={(self.manual_billing if hasattr(self, "manual_billing") else None)!r}, '
                f'indirect_acceptor={(self.indirect_acceptor if hasattr(self, "indirect_acceptor") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'start_at={(self.start_at if hasattr(self, "start_at") else None)!s}, '
                f'interval={(self.interval if hasattr(self, "interval") else None)!s}, '
                f'interval_count={(self.interval_count if hasattr(self, "interval_count") else None)!s}, '
                f'billing_type={(self.billing_type if hasattr(self, "billing_type") else None)!s}, '
                f'current_cycle={(self.current_cycle if hasattr(self, "current_cycle") else None)!s}, '
                f'payment_method={(self.payment_method if hasattr(self, "payment_method") else None)!s}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!s}, '
                f'installments={(self.installments if hasattr(self, "installments") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'customer={(self.customer if hasattr(self, "customer") else None)!s}, '
                f'card={(self.card if hasattr(self, "card") else None)!s}, '
                f'items={(self.items if hasattr(self, "items") else None)!s}, '
                f'statement_descriptor={(self.statement_descriptor if hasattr(self, "statement_descriptor") else None)!s}, '
                f'metadata={(self.metadata if hasattr(self, "metadata") else None)!s}, '
                f'setup={(self.setup if hasattr(self, "setup") else None)!s}, '
                f'gateway_affiliation_id={(self.gateway_affiliation_id if hasattr(self, "gateway_affiliation_id") else None)!s}, '
                f'next_billing_at={(self.next_billing_at if hasattr(self, "next_billing_at") else None)!s}, '
                f'billing_day={(self.billing_day if hasattr(self, "billing_day") else None)!s}, '
                f'minimum_price={(self.minimum_price if hasattr(self, "minimum_price") else None)!s}, '
                f'canceled_at={(self.canceled_at if hasattr(self, "canceled_at") else None)!s}, '
                f'discounts={(self.discounts if hasattr(self, "discounts") else None)!s}, '
                f'increments={(self.increments if hasattr(self, "increments") else None)!s}, '
                f'boleto_due_days={(self.boleto_due_days if hasattr(self, "boleto_due_days") else None)!s}, '
                f'split={(self.split if hasattr(self, "split") else None)!s}, '
                f'boleto={(self.boleto if hasattr(self, "boleto") else None)!s}, '
                f'manual_billing={(self.manual_billing if hasattr(self, "manual_billing") else None)!s}, '
                f'indirect_acceptor={(self.indirect_acceptor if hasattr(self, "indirect_acceptor") else None)!s})')
