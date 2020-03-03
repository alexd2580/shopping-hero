import graphene
from shopping_hero.schemas.shop import Shop
from shopping_hero.core.shop import list_shops


class Query(graphene.ObjectType):
    shops = graphene.List(Shop)

    def resolve_shops(self, info, *args, **kwargs):
        print(args)
        print(kwargs)
        return list_shops()
