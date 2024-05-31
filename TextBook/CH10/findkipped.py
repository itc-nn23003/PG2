import os
import re

def fill_missing_numbers(directory, prefix):
    # 指定されたディレクトリのファイルリストを取得
    files = os.listdir(directory)
    
    # 接頭辞と連番にマッチするファイルを抽出
    pattern = re.compile(rf'^{prefix}(\d+)\.txt$')
    matched_files = [(f, int(pattern.match(f).group(1))) for f in files if pattern.match(f)]
    
    # 連番順にソート
    matched_files.sort(key=lambda x: x[1])
    
    # 欠けている番号を見つけてファイル名を変更
    expected_number = 1
    for file, number in matched_files:
        if number != expected_number:
            new_file_name = f"{prefix}{expected_number:03}.txt"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
        expected_number += 1

# 使用例
directory = '/home/vagrant/PG2/TextBook/CH10'
prefix = 'spam'
fill_missing_numbers(directory, prefix)

