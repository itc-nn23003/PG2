#! python3 - マルチクリップボードプログラム
# mclip.py

TEXT = {'agree': 'そうですね。私も賛成します。それがいいと思います。',
        'busy': 'すみませんが、今週後半か来週にしていただけませんか？',
        'upsell': 'それを毎月の寄付にすることを検討いただけませんか？'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python3 mclip.py [キーフレーズ名]')
    print('キーフレーズに対応するテキストをクリップボードにコピーします。')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(keyphrase + 'のテキストをクリップボードにコピーしました。')
else:
    print(keyphrase + 'に対応するテキストはありません。')

