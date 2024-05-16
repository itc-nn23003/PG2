import ast
def is_valid_chess_board(board):
    piece_count = {
        'bking': 0,
        'wking': 0,
        'bqueen': 0,
        'wqueen': 0,
        'bbishop': 0,
        'wbishop': 0,
        'brook': 0,
        'wrook': 0,
        'bknight': 0,
        'wknight': 0,
        'bpawn': 0,
        'wpawn': 0,
    }
    max_piece_count = {
        'bking': 1,
        'wking': 1,
        'bqueen': 1,
        'wqueen': 1,
        'bbishop': 2,
        'wbishop': 2,
        'brook': 2,
        'wrook': 2,
        'bknight': 2,
        'wknight': 2,
        'bpawn': 8,
        'wpawn': 8,
    }
    def is_valid_position(pos):
        if len(pos) != 2:
            return False
        col, row = pos[0], pos[1]
        return col in 'abcdefgh' and row in '12345678'
    for pos, piece in board.items():
        if not is_valid_position(pos):
            return False
        if piece not in piece_count:
            return False
        piece_count[piece] += 1
        if piece_count[piece] > max_piece_count[piece]:
            return False
    if piece_count['bking'] != 1 or piece_count['wking'] != 1:
        return False
    return True
input_str = input("チェス盤の状態を辞書形式で入力してください: ")
try:
    chess_board = ast.literal_eval(input_str)
    if isinstance(chess_board, dict):
        print(is_valid_chess_board(chess_board))
    else:
        print("入力が辞書形式ではありません。")
except (SyntaxError, ValueError):
    print("入力が無効です。正しい辞書形式で入力してください。")