import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Product
from django.db.models import Count, Sum
from django.db.models.functions import Cast
from django.db import models


class ProductType(DjangoObjectType):
    total_products = graphene.Int()

    def resolve_total_products(parent, info, **kwargs):
        return Product.objects.filter(user=parent).aggregate(Count('id'))['id__count']


    class Meta:
        model = Product
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'price': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
        fields = '__all__'

