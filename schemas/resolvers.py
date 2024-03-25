import typing
import urllib.parse
from schemas.types import BookInfo, IndustryIdentifier, ImageLinks
# from schemas.data import bookData
import httpx


API_KEY = "AIzaSyDmLXYIH0UVZ23GapjdDVUxgR0iOhKI-S0"
#API_KEY = "Descomentar"
BASE_URL = "https://www.googleapis.com/books/v1/volumes"


def searchGBooks_resolver(
    self,
    info,
    author: typing.Optional[str] = None,
    isbn: typing.Optional[str] = None,
    title: typing.Optional[str] = None,
    page: typing.Optional[int] = 1,
    items_per_page: typing.Optional[int] = 10,
) -> typing.List[BookInfo]:

    params = {
        "key": API_KEY,
    }

    query_parts = []
    if author is not None:
        query_parts.append(f"inauthor:{author}")
    if isbn is not None:
        query_parts.append(f"isbn:{isbn}")
    if title is not None:
        query_parts.append(f"intitle:{title}")  # Use +intitle for exact title match

    if query_parts:
        params["q"] = "+".join(query_parts)

    params["startIndex"] = (page - 1) * items_per_page
    params["maxResults"] = items_per_page


    try:
        with httpx.Client() as client:
            response = client.get(f"{BASE_URL}?{urllib.parse.urlencode(params)}")
            response.raise_for_status()  # Raise exception for non-2xx status codes
            response_data = response.json()
        books = []

        for book_data in response_data.get("items", []):

            # Assuming your response has "volumeInfo" key with book details
            book_id = book_data.get("id", "")  # Obtendo o ID do livro
            book_info = book_data.get("volumeInfo", {})
            autores = book_info.get("authors", [])
            industry_identifiers = [
                IndustryIdentifier(
                    type=identifier_data.get("type", ""),
                    identifier=identifier_data.get("identifier", ""),
                )
                for identifier_data in book_info.get("industryIdentifiers", [])
            ]
            image_links = ImageLinks(

                smallThumbnail=book_info.get("imageLinks", {}).get("smallThumbnail", ""),
                thumbnail=book_info.get("imageLinks", {}).get("thumbnail", ""),
            )

            new_book = BookInfo(

                IdGoogle=book_id,    
                title=book_info.get("title", ""),
                subtitle=book_info.get("subtitle", ""),
                autores=autores,
                publisher=book_info.get("publisher", ""),
                publishedDate=book_info.get("publishedDate", ""),
                description=book_info.get("description", ""),
                industryIdentifiers=industry_identifiers,
                pageCount=book_info.get("pageCount", 0),
                printType=book_info.get("printType", ""),
                categories=book_info.get("categories", []),
                averageRating=book_info.get("averageRating", 0.0),
                ratingsCount=book_info.get("ratingsCount", 0),
                imageLinks=image_links,
                language=book_info.get("language", ""),

            )

            books.append(new_book)

        return books

    except Exception as e:
        print(f"Error fetching books from Google Books: {e}")
        return [] 


    