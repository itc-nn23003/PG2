import sys
import openpyxl

# コマンドライン引数の取得とバリデーション
if len(sys.argv) != 4:
    print("Usage: python script.py <N> <M> <file_name>")
    sys.exit(1)

# 引数を取得
n = int(sys.argv[1])
m = int(sys.argv[2])
file_name = sys.argv[3]

# スプレッドシートを読み込み
wb = openpyxl.load_workbook(file_name)
ws = wb.active

# 指定された行に空行を挿入
ws.insert_rows(n + 1, m)

# 新しいスプレッドシートとして保存
output_file_name = f"modified_{file_name}"
wb.save(output_file_name)

