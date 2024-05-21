import requests
from bs4 import BeautifulSoup
import re

def index():
    url = 'https://www.bonbast.com'
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Referer': url,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8,de;q=0.7',
        'Cache-Control': 'no-cache',
        'Dnt': '1',
        'Origin': url,
        'Pragma': 'no-cache',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Requested-With': 'XMLHttpRequest',
    }

    response = session.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    scripts = soup.find_all('script')
    param = None
    for script in scripts:
        if '$.post' in script.text:
            match = re.search(r'param:\s*"([^"]+)"', script.text)
            if match:
                param = match.group(1)
                break

    if param:
        post_url = url + '/json'
        post_data = {
            'param': param,
        }

        # درخواست POST
        response = session.post(post_url, headers=headers, data=post_data)

        data = response.json()

        # تصحیح داده‌های ارزی
        currencies_data = {}
        for key, value in data.items():
            if key.endswith('1'):
                currency = key[:-1]
                if currency not in currencies_data:
                    currencies_data[currency] = {'sell': value}
                else:
                    currencies_data[currency]['sell'] = value
            elif key.endswith('2'):
                currency = key[:-1]
                if currency not in currencies_data:
                    currencies_data[currency] = {'buy': value}
                else:
                    currencies_data[currency]['buy'] = value

        return currencies_data
    else:
        return {'error': 'param not found'}, 400


# اجرای متد index
result = index()
print(result)
