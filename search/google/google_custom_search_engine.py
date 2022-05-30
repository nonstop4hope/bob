import math
import os

from googleapiclient.discovery import build


class GoogleCSE:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.cse_id = os.getenv('GOOGLE_CSE_ID')
        self.num_results = int(os.getenv('NUM_RESULTS'))

    def search(self, search_term, **kwargs):
        service = build("customsearch", "v1", developerKey=self.api_key)
        if self.num_results > 100:
            raise NotImplementedError('Google Custom Search API supports max of 100 results')
        elif self.num_results > 10:
            kwargs['num'] = 10
            calls_to_make = math.ceil(self.num_results / 10)
        else:
            calls_to_make = 1
        kwargs['start'] = start_item = 1
        items_to_return = []

        while calls_to_make > 0:
            res = service.cse().list(q=search_term, cx=self.cse_id, **kwargs).execute()
            items_to_return.extend(res['items'])
            calls_to_make -= 1
            start_item += 10
            kwargs['start'] = start_item
            leftover = self.num_results - start_item + 1
            if 0 < leftover < 10:
                kwargs['num'] = leftover

        return items_to_return
