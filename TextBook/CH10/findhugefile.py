import os

def get_size(path):
    """ディレクトリのサイズを再帰的に取得する関数"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # ファイルが存在するかどうか確認（シンボリックリンクなどの問題を回避）
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def find_large_files_and_directories(root_dir, size_threshold):
    """指定されたディレクトリツリーを渡り歩いて、大きなファイルやディレクトリを探す関数"""
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for name in filenames:
            filepath = os.path.join(dirpath, name)
            if os.path.exists(filepath):  # ファイルが存在するか確認
                try:
                    if os.path.getsize(filepath) > size_threshold:
                        print(f"Large file: {os.path.abspath(filepath)}")
                except FileNotFoundError:
                    # ファイルが見つからない場合はスキップ
                    continue

        for name in dirnames:
            dirpath_full = os.path.join(dirpath, name)
            if os.path.exists(dirpath_full):  # ディレクトリが存在するか確認
                try:
                    dir_size = get_size(dirpath_full)
                    if dir_size > size_threshold:
                        print(f"Large directory: {os.path.abspath(dirpath_full)}")
                except FileNotFoundError:
                    # ディレクトリが見つからない場合はスキップ
                    continue

# メインプログラム
if __name__ == "__main__":
    root_directory = '/'  # ここを探索したいディレクトリに変更してください
    size_threshold = 100 * 1024 * 1024  # 100MB

    find_large_files_and_directories(root_directory, size_threshold)

