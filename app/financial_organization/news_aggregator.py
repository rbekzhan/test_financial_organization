import requests


class NewsAggregator:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_news(self, query, source='all', language='en', page_size=10):
        base_url = 'https://newsapi.org/v2/everything'
        headers = {'X-Api-Key': self.api_key}
        params = {
            'q': query,
            'sources': source,
            'language': language,
            'pageSize': page_size
        }

        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()['articles']
        else:
            return f"Failed to fetch news. Status code: {response.status_code}"


# Пример использования
api_key = 'NEWS_API_KEY'
aggregator = NewsAggregator(api_key)

# Получение новостей по запросу "technology"
news = aggregator.get_news(query='technology')
