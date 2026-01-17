import requests

def get_news_data(api_key):
    url = f'https://newsapi.org/v2/everything?q=cybersecurity&apiKey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        return []
