# リスト7.1 演習用のvenv環境を構築(macOS、Linux)

#$ mkdir scraping
#$ cd scraping
#$ python3 -m venv env
#$ source env/bin/activate
#(env) $ pip install requests
#(env) $ pip install beautifulsoup4

# リスト7.2 演習用のvenv環境を構築(Windows)

#> mkdir scraping
#> cd scraping
#> python -m venv env
#> env\Scripts\Activate.ps1
#(env) > pip install requests
#(env) > pip install beautifulsoup4

# リスト7.3 events.py

#import requests

#def main():
#    params = {
#        'keyword': 'python',
#        'ym': '201812',
#    }
#    url = 'https://connpass.com/api/v1/event/'
#    r = requests.get(url, params=params)
#    event_info = r.json()  # レスポンスのJSONを変換

#    print('件数:', event_info['results_returned'])  # 件数を表示
#    for event in event_info['events']:
#        print(event['title'])
#        print(event['started_at'])

#if __name__ == '__main__':
#    main()

# リスト7.4 connpass APIを実行

#(env) $ python events.py
#件数: 10
#【超初心者対象】プログラミング未経験者が初心者になるためのPython体験@池袋
#2018-11-28T19:00:00+09:00
#【初心者歓迎】大阪Python もくもく会 #1
#2018-11-16T19:00:00+09:00
#[R]『Ｒ統計解析パーフェクトマスター』１冊丸ごと演習会
#2018-11-23T14:00:00+09:00
#:

# リスト7.11 simple.py

#import requests
#from bs4 import BeautifulSoup

#def main():
#    url = 'https://pycon.jp/2017/ja/sponsors/'
#    res = requests.get(url)
#    content = res.content
#    soup = BeautifulSoup(content, 'html.parser')
#    sponsors = soup.find_all('div', class_='sponsor-content')
#    for sponsor in sponsors:
#        url = sponsor.h3.a['href']
#        name = sponsor.h4.text
#        print(name, url)

#if __name__ == '__main__':
#    main()

# リスト7.12 スクレイピングを実行

#(env) $ python simple.py
#株式会社SQUEEZE https://squeeze-inc.co.jp/
#株式会社MonotaRO https://recruit.monotaro.com/?utm_medium=outside_flier&utm_source=pycon.jp&utm_campaign=PyConJP2017
#LINE株式会社 https://engineering.linecorp.com/
#Retty株式会社 http://corp.retty.me/
#iRidge, Inc. https://iridge.jp/
#株式会社いい生活 http://www.e-seikatsu.info/recruit/graduate/
#:

# リスト7.20 認証付きURLにアクセスする

# import requests
# r = requests.get('https://api.github.com/user', auth=('nagata4139', 'pass'))
# r.status_code

# リスト7.21 requests で POST する

# payload = {'key1': 'value1', 'key2': 'value2'} # POST するパラメーター
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

# リスト7.22 requests でパラメーター付で GET する

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)

# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)

# リスト7.23 Beautiful Soup 4の使用例

#import requests
#from bs4 import BeautifulSoup
#r = requests.get('https://www.python.org/blogs/')
#soup = BeautifulSoup(r.content, 'html.parser') # 取得したHTMLを解析
#soup.title # titleタグの情報を取得

#soup.title.name

#soup.title.string # titleタグの文字列を取得

#soup.a

#len(soup.find_all('a')) # 全ての a タグを取得しt len() で件数を取得

# リスト7.24 find/find_all の使用例

#len(soup.find_all('h1')) # 指定したタグを検索

#len(soup.find_all(['h1', 'h2', 'h3'])) # 複数のタグのいずれかにマッチ

#len(soup.find_all('h3', {'class': 'event-title'})) # <h3 class="event-title"> にマッチ