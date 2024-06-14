import os
import sys
import requests
import bs4
import re
from urllib.parse import urljoin

# 引数の数をチェック
if len(sys.argv) != 2:
    sys.exit('使い方: python checkurl.py URL')

# 保存ディレクトリを作成
DIR = 'files'
os.makedirs(DIR, exist_ok=True)

# 入力URLを取得
url = sys.argv[1]

# URLにリクエストを送信
res = requests.get(url)
res.raise_for_status()

# BeautifulSoupでHTMLを解析
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# aタグを検索
links = soup.select('a')

# ダウンロード済みURLを管理するセット
href_set = set()

for link in links:
    # aタグのhref属性を取得
    href = link.get('href')
    if not href:
        continue

    # 相対パスの場合は正規化
    if not href.startswith('http'):
        href = urljoin(url, href)

    # '#ラベル' を削除
    href = re.sub(r'(#.+)', '', href)

    # 過去にダウンロードしたURLは省く
    if href in href_set:
        continue
    href_set.add(href)

    print(href, end='', flush=True)

    try:
        # リンク先をダウンロード
        res = requests.get(href)
        res.raise_for_status()

        # ファイル名を生成
        filename = re.sub(r'^(https?://)', '', href)
        filename = re.sub(r'[/~?&+]', '_', filename)

        # ファイルに保存
        with open(os.path.join(DIR, filename), 'wb') as hfile:
            for chunk in res.iter_content(100000):
                hfile.write(chunk)
        print(' ->', filename, 'に保存')

    except requests.exceptions.HTTPError as e:
        if res.status_code == 404:
            print(' -> 404 Not Found')
        else:
            print(' -> HTTP Error:', e)

    except requests.exceptions.RequestException as e:
        print(' -> Request Error:', e)

    except Exception as e:
        print(' -> Error:', e)
