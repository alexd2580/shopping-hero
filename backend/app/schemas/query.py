import graphene
from app.core.shop import list_shops
from app.schemas.shop import Shop


class Query(graphene.ObjectType):
    shops = graphene.List(Shop)

    def resolve_shops(self, info, *args, **kwargs):
        print(args)
        print(kwargs)
        return list_shops()
