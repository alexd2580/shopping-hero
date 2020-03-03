import graphene


def build_resolvers(exclude=()):
    def make_resolver(field):
        return lambda root, info, *args, **kwargs: getattr(root, field)

    def needs_resolver(field):
        return not field.startswith("_") and field not in exclude

    def transform_class(cls):
        fields = [field for field in vars(cls).keys() if needs_resolver(field)]
        for field in fields:
            setattr(cls, f"resolve_{field}", make_resolver(field))
        return cls

    return transform_class


@build_resolvers()
class Shop(graphene.ObjectType):
    id = graphene.UUID()
    name = graphene.String()
    latitude = graphene.Float()
    longitude = graphene.Float()
    opens_at = graphene.Time()
    closes_at = graphene.Time()
