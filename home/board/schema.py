import strawberry
import strawberry_django

from . import types


@strawberry.type
class Query:
    topic: types.Topic = strawberry_django.node()
    topics: strawberry_django.relay.ListConnectionWithTotalCount[types.Topic] = (
        strawberry_django.connection()
    )
    comment: types.Comment = strawberry_django.node()
    comments: strawberry_django.relay.ListConnectionWithTotalCount[types.Comment] = (
        strawberry_django.connection()
    )
