import os
import openpyxl

# Excelファイルの作成
wb = openpyxl.Workbook()
ws = wb.active

# カレントディレクトリ（.）内のすべての.txtファイルの内容をExcelに書き込む
col_index = 1
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for row_index, line in enumerate(lines, start=1):
                cell = ws.cell(row=row_index, column=col_index)
                cell.value = line.strip()  # 行末の改行文字を削除して書き込む
        col_index += 1

# Excelファイルを保存
output_excel = 'texts.xlsx'
wb.save(output_excel)

