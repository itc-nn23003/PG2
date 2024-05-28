import pyinputplus as pyip

# メニューの値段設定
prices = {
    'パン': {'小麦粉パン': 50, '白パン': 40, 'サワー種': 60},
    'プロテイン': {'チキン': 100, 'ターキー': 120, 'ハム': 80, '豆腐': 90},
    'チーズ': {'チェダー': 30, 'スイス': 35, 'モツァレラ': 40},
    '追加': {'マヨネーズ': 10, 'からし': 10, 'レタス': 20, 'トマト': 20}
}

# ユーザーにパンの種類を尋ねる
bread = pyip.inputMenu(['小麦粉パン', '白パン', 'サワー種'], prompt='パンの種類を選んでください:\n')
# ユーザーにタンパク質の種類を尋ねる
protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt='タンパク質の種類を選んでください:\n')
# チーズが必要か尋ねる
cheese_needed = pyip.inputYesNo('チーズは必要ですか？ (yes/no)\n')

if cheese_needed == 'yes':
    # チーズの種類を尋ねる
    cheese = pyip.inputMenu(['チェダー', 'スイス', 'モツァレラ'], prompt='チーズの種類を選んでください:\n')
else:
    cheese = None

# 各追加のトッピングが必要か尋ねる
mayo = pyip.inputYesNo('マヨネーズは必要ですか？ (yes/no)\n')
mustard = pyip.inputYesNo('からしは必要ですか？ (yes/no)\n')
lettuce = pyip.inputYesNo('レタスは必要ですか？ (yes/no)\n')
tomato = pyip.inputYesNo('トマトは必要ですか？ (yes/no)\n')

# サンドイッチの数を尋ねる
num_sandwiches = pyip.inputInt('いくつサンドイッチが欲しいですか？ (1以上の数字)\n', min=1)

# 合計金額を計算する
total_cost = prices['パン'][bread] + prices['プロテイン'][protein]

if cheese:
    total_cost += prices['チーズ'][cheese]

if mayo == 'yes':
    total_cost += prices['追加']['マヨネーズ']
if mustard == 'yes':
    total_cost += prices['追加']['からし']
if lettuce == 'yes':
    total_cost += prices['追加']['レタス']
if tomato == 'yes':
    total_cost += prices['追加']['トマト']

total_cost *= num_sandwiches

# 結果を表示する
print(f"選択したサンドイッチの合計金額は {total_cost} 円です。")

