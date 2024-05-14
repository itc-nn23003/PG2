def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


print('整数を入力してください:')
while True:
    try:
        type_number = int(input())
        break
    except ValueError:
        print('有効な整数を入力してください。')
        
while type_number != 1:
    type_number = collatz(type_number)
    print(type_number)

print('終了します。')
        
    
