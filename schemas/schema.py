import typing
import strawberry

from schemas.types import BookInfo
from schemas.resolvers import searchGBooks_resolver




@strawberry.type
class QueryProducao:
  
    @strawberry.field
    def searchGBooks(
    self,
    info,
    author: typing.Optional[str] = None,
    isbn: typing.Optional[str] = None,
    title: typing.Optional[str] = None,
    page: typing.Optional[int] = 1,  # Página padrão é 1
    items_per_page: typing.Optional[int] = 12,  
) -> typing.List[BookInfo]:
     return searchGBooks_resolver(self, info, author, isbn, title, page, items_per_page) 
