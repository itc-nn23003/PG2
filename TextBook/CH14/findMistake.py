import ezsheets

# Google Sheetsのスプレッドシートを取得
ss = ezsheets.Spreadsheet('1Uk3w3JdAcps9UNfZrlzHu2ocMML8yobVUyBgXsa1Hh0')

# スプレッドシートの最初のシートを取得
sheet = ss[0]

# 行をチェックして、間違っている行を見つける
for row_num in range(2, sheet.rowCount + 1):  # ヘッダー行をスキップするために2から始める
    row = sheet.getRow(row_num)
    
    # 右側の空白セルを削除
    row = [cell for cell in row if cell != '']
    
    # 空白行をチェック
    if not row:
        break

    try:
        bean_per_jar = int(row[0])
        jars = int(row[1])
        total_beans = int(row[2])

        if bean_per_jar * jars != total_beans:
            print(f'間違いがある行番号: {row_num}, データ: {row}')
    except ValueError:
        print(f'行番号 {row_num} に無効なデータがあります: {row}')

print('チェックが完了しました。')
