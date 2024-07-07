import strawberry
from strawberry.tools import merge_types
from strawberry_django.optimizer import DjangoOptimizerExtension

import home.board.schema
import home.users.schema

Query = merge_types(
    "Query",
    (
        home.users.schema.Query,
        home.board.schema.Query,
    ),
)

schema = strawberry.Schema(
    query=Query,
    # https://strawberry-graphql.github.io/strawberry-django/guide/optimizer/
    extensions=[DjangoOptimizerExtension],
)
