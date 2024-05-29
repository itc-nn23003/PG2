#! python3
# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save <keyword> - クリップボードをキーワードに紐付けて保存
# py.exe mcb.pyw <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
# py.exe mcb.pyw list - 全キーワードをクリップボードにコピー

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # キーワード一覧と、内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()

