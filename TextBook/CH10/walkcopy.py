import os
import shutil

def copy_files_with_extension(src_dir, dest_dir, extensions):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, _, files in os.walk(src_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)

                # ファイル名が重複しないようにする
                dest_file_path = avoid_overwrite(dest_file_path)

                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied {src_file_path} to {dest_file_path}")

def avoid_overwrite(file_path):
    base, extension = os.path.splitext(file_path)
    counter = 1
    new_file_path = file_path
    while os.path.exists(new_file_path):
        new_file_path = f"{base} ({counter}){extension}"
        counter += 1
    return new_file_path

# 使用例
src_directory = "./Pictures"
dest_directory = "/"
extensions_to_copy = ['.pdf', '.jpg']  # コピー対象の拡張子のリスト

copy_files_with_extension(src_directory, dest_directory, extensions_to_copy)

