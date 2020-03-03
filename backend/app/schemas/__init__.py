import graphene
from app.schemas.query import Query

schema = graphene.Schema(query=Query)
