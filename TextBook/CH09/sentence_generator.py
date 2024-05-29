import os

def replace_keywords_in_text(file_path):
    # ファイルの存在を確認する
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # ファイルからテキストを読み込む
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # ユーザーから入力を求める
    adjective = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")

    # テキスト内のキーワードを置換する
    replaced_text = text.replace('ADJECTIVE', adjective)
    replaced_text = replaced_text.replace('NOUN', noun1, 1)  # 1つ目のNOUNを置換
    replaced_text = replaced_text.replace('NOUN', noun2, 1)  # 2つ目のNOUNを置換
    replaced_text = replaced_text.replace('VERB', verb)

    # 置換後のテキストを表示する
    print("\nReplaced Text:\n")
    print(replaced_text)

    # 新しいファイルに保存する
    new_file_path = 'replaced_text.txt'
    try:
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(replaced_text)
        print(f"\nThe replaced text has been saved to {new_file_path}.")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

# 使用するテキストファイルのパスを指定
file_path = 'text.txt'
replace_keywords_in_text(file_path)

