import graphene
from collections import namedtuple
from .schemaClass.playDataSchema import playDataSchema
from graphene_django import DjangoObjectType

from django.db.models import Q

from .models import URL
from .models import Category, Ingredient
from .models import Customer, Order, OrderItem, OrderItemDetail


class URLTpye(DjangoObjectType):
    class Meta:
        model = URL


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


# 顧客
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer


# 訂單
class OrderType(DjangoObjectType):
    class Meta:
        model = Order


# 訂購項目
class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem


# 訂購項目明細
class OrderItemDetailType(DjangoObjectType):
    class Meta:
        model = OrderItemDetail

# 查詢


class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String(default_value='t'))

    def resolve_reverse(self, info, word):
        print(self)
        return 'hello'

    urls = graphene.List(URLTpye, url=graphene.String())

    def resolve_urls(self, info, url=None, **kwargs):
        queryset = URL.objects.all()

        if url:

            _filter = Q(full_url_icontains=url)
            queryset = queryset.filter(_filter)

        return queryset

    category = graphene.List(CategoryType)

    category2 = graphene.Field(
        CategoryType, id=graphene.Int(), name=graphene.String())

    Ingredient = graphene.List(IngredientType)

    def resolve_category(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category2(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

    customerList = graphene.List(CustomerType)

    customer = graphene.Field(
        CustomerType,
        id=graphene.Int(),
        name=graphene.String(),
        tel=graphene.String(),
        phone=graphene.String(),
        date=graphene.Date(),
        other=graphene.String()
    )

    def resolve_customerList(self, info, **kwargs):
        return Customer.objects.all()

    def resolve_customer(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        tel = kwargs.get('tel')
        phone = kwargs.get('phone')
        date = kwargs.get('date')

        if id is not None:
            return Customer.objects.get(pk=id)

        if name is not None:
            return Customer.objects.get(name=name)

        if tel is not None:
            return Customer.objects.get(tel=tel)
        if phone is not None:
            return Customer.objects.get(phone=phone)
        if date is not None:
            return Customer.objects.get(date=date)

    orderList = graphene.List(OrderType)

    order = graphene.Field(
        OrderType,
        id=graphene.Int(),
        ord_name=graphene.String(),
        ord_address=graphene.String(),
        ord_mapid=graphene.String(),
        ord_tolprice=graphene.Int(),
        ord_startdate=graphene.Date(),
        ord_enddate=graphene.Date(),
        ord_other=graphene.String(),
        ord_customer=graphene.Int()
    )

    def resolve_orderList(self, info, **kwargs):
        return Order.objects.all()

    def resolve_order(self, info, **kwargs):
        id = kwargs.get('id')
        ord_name = kwargs.get('ord_name')
        ord_address = kwargs.get('ord_address')
        ord_mapid = kwargs.get('ord_mapid')
        ord_tolprice = kwargs.get('ord_tolprice')
        ord_startdate = kwargs.get('ord_startdate')
        ord_enddate = kwargs.get('ord_enddate')
        ord_other = kwargs.get('ord_other')
        ord_customer = kwargs.get('ord_customer')

        if id is not None:
            return Order.objects.get(pk=id)

        if ord_name is not None:
            return Order.objects.get(ord_name=ord_name)

        if ord_address is not None:
            return Order.objects.get(ord_address=ord_address)
        if ord_mapid is not None:
            return Order.objects.get(ord_mapid=ord_mapid)
        if ord_tolprice is not None:
            return Order.objects.get(ord_tolprice=ord_tolprice)
        if ord_startdate is not None:
            return Order.objects.get(ord_startdate=ord_startdate)
        if ord_enddate is not None:
            return Order.objects.get(ord_enddate=ord_enddate)
        if ord_customer is not None:
            return Order.objects.get(ord_customer=ord_customer)


""" Query{
  category2(name:"Meat") {
		id
    name
  }
} """


def resolve_ingredient(self, info, **kwargs):
    return Ingredient.objects.select_related('category').all()


class CreateURL(graphene.Mutation):
    url = graphene.Field(URLTpye)

    class Arguments:
        full_url = graphene.String()

    def mutate(self, info, full_url):
        url = URL(full_url=full_url)
        url.save()

        return CreateURL(url=url)


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class CreateCategory(graphene.Mutation):

    class Arguments:
        input = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, input=None):
        category_instance = Category(name=input.name)
        category_instance.save()
        return CreateCategory(category=category_instance)


class CreateCustomer(graphene.Mutation):
    customer = graphene.Field(CustomerType)

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        tel = graphene.String()
        phone = graphene.String()
        date = graphene.Date()
        other = graphene.String()

    def mutate(self, info, id, name, tel, phone, date, other):
        customer_instance = Customer(
            id=id, name=name, tel=tel, phone=phone, date=date, other=other)
        customer_instance.save()
        return CreateCustomer(customer=customer_instance)


class CreateOrder(graphene.Mutation):
    order = graphene.Field(OrderType)

    class Arguments:
        id = graphene.Int()
        ord_name = graphene.String()
        ord_address = graphene.String()
        ord_mapid = graphene.String()
        ord_tolprice = graphene.Int()
        ord_startdate = graphene.Date()
        ord_enddate = graphene.Date()
        ord_other = graphene.String()
        ord_customer = graphene.Int()

    def mutate(self, info, id, ord_name, ord_address, ord_mapid, ord_tolprice, ord_startdate, ord_enddate, ord_other, ord_customer):
        order_instance = Customer(
            id=id, ord_name=ord_name, ord_address=ord_address, ord_mapid=ord_mapid, ord_tolprice=ord_tolprice, ord_startdateother=ord_startdate,
            ord_enddate=ord_enddate, ord_other=ord_other, ord_customer=ord_customer
        )
        order_instance.save()
        return CreateOrder(order=order_instance)


class Mutation(graphene.ObjectType):
    create_url = CreateURL.Field()
    create_category = CreateCategory.Field()
    create_customer = CreateCustomer.Field()
    create_order = CreateOrder.Field()


schema = graphene.Schema(query=Query)
