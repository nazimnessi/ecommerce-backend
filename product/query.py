import graphene
from graphene_django.filter import DjangoFilterConnectionField

from product.node import ProductType
from .models import Product


class Query(graphene.ObjectType):
    all_products = DjangoFilterConnectionField(ProductType)

    def resolve_all_products(root, info, **kwargs):
        queryset = Product.objects.all()
        return queryset.order_by('-id')
