import strawberry
import strawberry_django
from strawberry import relay

from . import models


@strawberry_django.type(models.Topic)
class Topic(relay.Node):
    comments: strawberry_django.relay.ListConnectionWithTotalCount["Comment"] = (
        strawberry_django.connection()
    )


@strawberry_django.type(models.Comment)
class Comment(relay.Node):
    body: strawberry.auto
