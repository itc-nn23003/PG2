import os
import re

def search_pattern_in_txt_files(directory, pattern):
    # コンパイルされた正規表現パターン
    regex = re.compile(pattern)
    
    # ディレクトリ内のファイルを探索
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if regex.search(line):
                            print(f"Match found in {file_path}: {line.strip()}")

# カレントディレクトリのパスを取得
directory_path = os.getcwd()
# メールアドレスを検索する正規表現パターン
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

search_pattern_in_txt_files(directory_path, pattern)

