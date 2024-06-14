# maplt.py - コマンドラインやクリップボードに指定した住所のちずを開く

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # コマンドラインから住所を取得する　mapIt.pyのあとに引数を指定して住所を入力できる
    address = ' '.join(sys.argv[1:])
    
else:
    # クリップボードから住所を取得する
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
