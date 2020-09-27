from django.db import models

from hashlib import md5
from django.db import models
# 錯誤處理
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from graphql import GraphQLError


# Create your models here.


class URL (models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        vadlidate = URLValidator()
        try:
            vadlidate(self.full_url)
        except ValidationError as e:
            raise GraphQLError('invalid url')

        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateField()
    other = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Order(models.Model):
    ord_name = models.TextField()
    ord_address = models.TextField()
    ord_mapid = models.TextField()
    ord_tolprice = models.IntegerField()
    ord_startdate = models.DateField()
    ord_enddate = models.DateField()
    ord_other = models.TextField()
    ord_customer = models.ForeignKey(
        Customer, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return self.ord_name


class OrderItem(models.Model):
    item_name = models.TextField()
    item_color = models.TextField()
    item_tpye = models.TextField()
    item_size = models.TextField()
    item_salary = models.IntegerField()
    item_time = models.TimeField()
    item_price = models.IntegerField()
    item_amount = models.IntegerField()
    item_order = models.ForeignKey(
        Order, related_name='orderitems', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class OrderItemDetail(models.Model):
    detail_name = models.TextField()
    detail_color = models.TextField()
    detail_tpye = models.TextField()
    detail_size = models.TextField()
    detail_price = models.IntegerField()
    detail_amount = models.IntegerField()
    detail_orderitem = models.ForeignKey(
        OrderItem, related_name='orderitemdetails', on_delete=models.CASCADE)

    def __str__(self):
        return self.detail_name
