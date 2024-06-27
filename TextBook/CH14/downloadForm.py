import ezsheets

# スプレッドシートIDを設定します
SPREADSHEET_ID = '1cK0BKk7JYQj-hi3GFZTw1a3G7DHdRVtd9POhY1q16xM'  # スプレッドシートIDを設定してください

# Googleスプレッドシートにアクセスするための認証を設定します
ss = ezsheets.Spreadsheet(SPREADSHEET_ID)

# シートを取得（通常、フォームの回答は最初のシートに格納されます）
sheet = ss[0]  # 最初のシートを取得します（シートのインデックスは0から始まります）

# 名前とメールアドレスを収集するリストを初期化
names_and_emails = []

# シートの全行を取得
rows = sheet.getRows()

# シートの行をループして、名前とメールアドレスを収集（ヘッダー行をスキップ）
for row in rows[1:]:  # 最初の行はヘッダーなので2行目から開始
    name = row[1]  # 2列目が名前であると仮定します
    email = row[2]  # 3列目がメールアドレスであると仮定します
    if name and email:  # 名前とメールアドレスが両方存在する場合のみ収集
        names_and_emails.append({'name': name, 'email': email})

# 収集した名前とメールアドレスを表示
for entry in names_and_emails:
    print(f"Name: {entry['name']}, Email: {entry['email']}")

