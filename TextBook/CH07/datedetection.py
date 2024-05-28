import re

# 日付を検出する正規表現
date_pattern = r'(?P<day>0[1-9]|[12][0-9]|3[01])/(?P<month>0[1-9]|1[0-2])/(?P<year>1[0-9]{3}|2[0-9]{3})'

# サンプルのテキスト
sample_text = """
31/01/2020
29/02/2020
30/02/2020
31/04/2021
28/02/2021
29/02/2021
15/06/2023
"""

# 正しい日付かどうか判別する関数
def is_valid_date(day, month, year):
    day = int(day)
    month = int(month)
    year = int(year)
    
    # 各月の日数
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # うるう年の判定
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29  # 2月は29日
    
    # 日付が正しいかどうか判定
    return 1 <= month <= 12 and 1 <= day <= month_days[month - 1]

# 正規表現で日付を検出し、判別する
for match in re.finditer(date_pattern, sample_text):
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    if is_valid_date(day, month, year):
        print(f'{day}/{month}/{year} は有効な日付です。')
    else:
        print(f'{day}/{month}/{year} は有効な日付ではありません。')

