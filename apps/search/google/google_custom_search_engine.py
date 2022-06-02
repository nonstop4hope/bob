import os
from dataclasses import dataclass, asdict

from googleapiclient.discovery import build


class GoogleCSE:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.cse_id = os.getenv('GOOGLE_CSE_ID')
        self.num_results = int(os.getenv('NUM_PAGES'))

    class GoogleResult:
        def __init__(self, title='N/A', description='N/A', url='N/A'):
            self.title = title
            self.description = description
            self.url = url

        def __iter__(self):
            return iter([('title', self.title), ('description', self.description), ('url', self.url)])

    def search_on_page(self, search_term: str, page_number: int):
        service = build("customsearch", "v1", developerKey=self.api_key)
        results = service.cse().list(q=search_term, cx=self.cse_id, start=page_number).execute()
        search_result = []
        for result in results['items']:
            element = self.GoogleResult()
            element.title = result.get('title')
            element.url = result.get('displayLink')
            element.description = result.get('snippet')
            search_result.append(dict(element))
        return search_result

    def search_on_multiply_pages(self, search_term: str):
        search_results = []
        for page in range(0, self.num_results):
            search_result = self.search_on_page(search_term, page)
            search_results.append(search_result)
        return search_results
