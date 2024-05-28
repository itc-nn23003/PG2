import re

def is_strong_password(password):
    # パスワードの長さが8文字以上であることを確認
    if len(password) < 8:
        return password, False
    
    # 大文字を含むか確認
    if not re.search(r'[A-Z]', password):
        return password, False
    
    # 小文字を含むか確認
    if not re.search(r'[a-z]', password):
        return password, False
    
    # 数字を含むか確認
    if not re.search(r'[0-9]', password):
        return password, False
    
    # すべての条件を満たす場合
    return password, True

# テスト例
print(is_strong_password("StrongPass1"))  # ("StrongPass1", True)
print(is_strong_password("weakpass"))     # ("weakpass", False)
print(is_strong_password("12345678"))     # ("12345678", False)
print(is_strong_password("Password"))     # ("Password", False)
print(is_strong_password("Pass1"))        # ("Pass1", False)

