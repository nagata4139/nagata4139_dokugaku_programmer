# リスト7.3 events.py

import requests

def main():
   params = {
       'keyword': 'python',
       'ym': '201812',
   }
   url = 'https://connpass.com/api/v1/event/'
   r = requests.get(url, params=params)
   event_info = r.json()  # レスポンスのJSONを変換

   print('件数:', event_info['results_returned'])  # 件数を表示
   for event in event_info['events']:
       print(event['title'])
       print(event['started_at'])

if __name__ == '__main__':
   main()