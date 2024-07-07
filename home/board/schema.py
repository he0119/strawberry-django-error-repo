import strawberry
import strawberry_django

from . import types


@strawberry.type
class Query:
    topics: strawberry_django.relay.ListConnectionWithTotalCount[types.Topic] = (
        strawberry_django.connection()
    )
