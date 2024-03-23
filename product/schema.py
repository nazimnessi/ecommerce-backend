import graphene
from .query import Query


schema_product = graphene.Schema(query=Query)
