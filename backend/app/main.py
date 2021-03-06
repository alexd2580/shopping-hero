import graphene
from app.schemas import schema
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.routing import Route

routes = [Route("/", GraphQLApp(schema=schema))]
app = Starlette(routes=routes)
