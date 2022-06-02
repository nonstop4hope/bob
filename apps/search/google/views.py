import json
from dataclasses import dataclass, field, asdict
from typing import List

from django.http import JsonResponse

from apps.search.google.google_custom_search_engine import GoogleCSE


@dataclass
class Response:
    error: bool = False
    message: str = ''
    results: List[GoogleCSE.GoogleResult] = field(default_factory=list)


def result(request):
    """Get google-search results via Google Custom Engine Search."""
    # Get search term from request body
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    search_term = body['search_term']

    # Get google search results
    google_search = GoogleCSE()
    google_response = Response()
    try:
        google_response.results = google_search.search_on_multiply_pages(search_term=search_term)
    except Exception as e:
        google_response.error = True
        google_response.message = e
        return JsonResponse(asdict(google_response), safe=False)
    return JsonResponse(asdict(google_response), safe=False)
