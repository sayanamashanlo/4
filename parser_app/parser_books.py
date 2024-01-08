import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = "https://mybook.ru/catalog/books/"

HEADERS = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

@csrf_exempt
def get_html(url, params=''):
    request_book = requests.get(url, headers=HEADERS, params=params)
    return request_book


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='e4xwgl-0 iJwsmp')
    books = []

    for item in items:
        books.append({
            'title_name': item.find('div', class_='e4xwgl-1 gEQwGK').get_text(),
            'descriptions': item.find('div', class_='e4xwgl-5 dgfgnj').get_text()
        })

    return books


@csrf_exempt
def book_parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_books = []
        for page in range(0, 1):
            html = get_html(f'https://mybook.ru/catalog/books/', params=page)
            all_books.extend(get_data(html.text))
        print(all_books)
        return all_books
    else:
        raise Exception('Error in parse')

book_parser()