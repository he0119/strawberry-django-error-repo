import strawberry
import strawberry_django
from strawberry.types import Info

from . import types


@strawberry.type
class Query:
    @strawberry_django.field()
    def viewer(self, info: Info) -> types.User:
        return info.context.request.user
