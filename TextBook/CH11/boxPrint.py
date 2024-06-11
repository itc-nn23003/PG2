def box_print(symbol, width, hight):
    if len(symbol) != 1:
        raise Exception('symbolは1文字の文字列でなければなりません。')
    if width <= 2:
        raise Exception('widthは2より大きくなければなりません。')
    if hight <= 2:
        raise Exception('hightは2より大きくなければなりません。')
    print(symbol * width)
    for i in range(hight - 2):
        print(symbol + (' ' * (width -2)) + symbol)
    print(symbol * width)
for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('例外が起こりました。: ' + str(err))