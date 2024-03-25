import typing
import strawberry

@strawberry.type
class IndustryIdentifier:
    type: str
    identifier: str
    
@strawberry.type
class ImageLinks:
    smallThumbnail: str
    thumbnail: str
  

@strawberry.type
class BookInfo:
    IdGoogle: str 
    title: str
    subtitle: str
    autores: typing.List[str]
    publisher: str
    publishedDate: str
    description: str
    industryIdentifiers: typing.List[IndustryIdentifier]
    pageCount: int
    printType: str
    categories: typing.List[str]  
    averageRating: float
    ratingsCount: int
    imageLinks: ImageLinks
    language: str