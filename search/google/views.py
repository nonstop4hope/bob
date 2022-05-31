import json

from django.http import HttpResponse
from search.google import google_custom_search_engine


def result(request):
    """Get google-search results via Google Custom Engine Search."""
    # Get search term from request body
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    search_term = body['search_term']

    # Get google search results
    google_search = google_custom_search_engine.GoogleCSE()
    try:
        results = google_search.search_on_multiply_pages(search_term=search_term)
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse(results, content_type='application/json')
