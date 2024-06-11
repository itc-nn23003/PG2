import random

guess = ''

# ユーザーの入力をバリデート
while guess not in ('表', '裏'):
    print('コインの裏表を当ててください。表か裏を入力してください。:')
    guess = input()

# コインの裏表をランダムに決定
toss = random.randint(0, 1)  # 0は裏、1は表

# 数値を文字列に変換して比較する
toss_str = '表' if toss == 1 else '裏'

# 結果を判定
if toss_str == guess:
    print('当たり!')
else:
    print('はずれ!もう一回当てて!')
    
    # 再入力をバリデート
    guess = ''
    while guess not in ('表', '裏'):
        guess = input()
    
    if toss_str == guess:
        print('当たり!')
    else:
        print('はずれ。このゲームは苦手ですね。')
