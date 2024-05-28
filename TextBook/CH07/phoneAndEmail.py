#! ptyhon3
#pythonAndEmail.py - クリップボードから電話番号とメアドを検索する

import pyperclip
import re

# 電話番号の正規表現を作る
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?         # 市外局番 (オプション)
    (\s|-|\.)?                 # 区切り文字 (オプション)
    (\d{3})                    # 最初の3桁
    (\s|-|\.)                  # 区切り文字
    (\d{4})                    # 最後の4桁
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 内線番号 (オプション)
)''', re.VERBOSE)

# 電子メールの正規表現を作る
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+          # ユーザー名
    @                          # @ 記号
    [a-zA-Z0-9.-]+             # ドメイン名
    (\.[a-zA-Z]{2,4})          # ドット-サムシング
)''', re.VERBOSE)

# クリップボードのテキストを検索する
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1] if groups[1] else '', groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# 検索結果をクリップボードに貼り付ける
if len(matches) > 0:
    s = '\n'.join(matches)
    pyperclip.copy(s)
    print('クリップボードにコピーしました')
    print(s)
else:
    print('電話番号やメールアドレスは見つかりませんでした。')
