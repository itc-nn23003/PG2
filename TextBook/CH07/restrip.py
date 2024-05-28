import re

def custom_strip(s: str, chars: str = None) -> str:
    if chars is None:
        # デフォルトの動作：空白文字を除去
        pattern = r'^\s+|\s+$'
    else:
        # 指定された文字を除去
        # 文字列をエスケープして正規表現パターンを作成
        escaped_chars = re.escape(chars)
        pattern = f'^[{escaped_chars}]+|[{escaped_chars}]+$'

    # 正規表現で文字列の両端から指定された文字を除去
    return re.sub(pattern, '', s)

# テストケース
print(custom_strip("  Hello, World!  "))  # "Hello, World!"
print(custom_strip("xxHello, World!xx", "x"))  # "Hello, World!"
print(custom_strip("abcHello, World!cba", "abc"))  # "Hello, World!"
import re

def custom_strip(s: str, chars: str = None) -> str:
    if chars is None:
        # デフォルトの動作：空白文字を除去
        pattern = r'^\s+|\s+$'
    else:
        # 指定された文字を除去
        # 文字列をエスケープして正規表現パターンを作成
        escaped_chars = re.escape(chars)
        pattern = f'^[{escaped_chars}]+|[{escaped_chars}]+$'

    # 正規表現で文字列の両端から指定された文字を除去
    return re.sub(pattern, '', s)

# テストケース
def test_custom_strip():
    test_cases = [
        ("  Hello, World!  ", None),
        ("xxHello, World!xx", "x"),
        ("abcHello, World!cba", "abc"),
    ]
    
    for s, chars in test_cases:
        stripped = custom_strip(s, chars)
        if chars is None:
            print(f"Original: '{s}' | Stripped: '{stripped}'")
        else:
            print(f"Original: '{s}' with chars '{chars}' | Stripped: '{stripped}'")

test_custom_strip()

