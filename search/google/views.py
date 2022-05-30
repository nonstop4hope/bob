from django.http import HttpResponse, JsonResponse
from search.google import google_custom_search_engine


def result(request):
    """Get google-search results via Google Custom Engine Search."""
    query = request.GET.get('q')
    google_search = google_custom_search_engine.GoogleCSE()
    try:
        results = google_search.search(search_term=query)
        return HttpResponse(results)
    except Exception as e:
        if str(e).find('Error 429'):
            return JsonResponse({'error': 'Quota exceeded for quota metric \'Queries\' and limit \'Queries per day\' '
                                          'of service \'customsearch.googleapis.com\''})
        return HttpResponse(e)
