import graphene
from shopping_hero.schemas.query import Query

schema = graphene.Schema(query=Query)
