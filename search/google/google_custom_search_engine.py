import json
import math
import os

from googleapiclient.discovery import build


class GoogleCSE:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.cse_id = os.getenv('GOOGLE_CSE_ID')
        self.num_results = int(os.getenv('NUM_PAGES'))

    class GoogleResult:
        def __init__(self):
            self.title = 'N/A'
            self.description = 'N/A'
            self.url = 'N/A'

        def to_json(self):
            return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=3)

    def search_on_page(self, search_term, page_number):
        service = build("customsearch", "v1", developerKey=self.api_key)
        results = service.cse().list(q=search_term, cx=self.cse_id, start=page_number).execute()
        search_result = []
        for result in results['items']:
            element = self.GoogleResult()
            element.title = result.get('title')
            element.url = result.get('displayLink')
            element.description = result.get('snippet')
            search_result.append(element.to_json())
        return search_result

    def search_on_multiply_pages(self, search_term):
        search_results = []
        for page in range(0, self.num_results):
            search_result = self.search_on_page(search_term, page)
            search_results.append(search_result)
        return search_results
