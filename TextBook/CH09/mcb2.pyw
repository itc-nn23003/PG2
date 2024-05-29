import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # クリップボードの内容を保存
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        # キーワード一覧をクリップボードにコピー
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        # キーワードの内容をクリップボードにコピー
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        # すべてのキーワードを削除
        mcb_shelf.clear()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf:
        # 特定のキーワードを削除
        del mcb_shelf[sys.argv[2]]

mcb_shelf.close()

