import pyinputplus as pyip

while True:
    prompt = 'バカを何時間も忙しくさせておく方法知りたいですか？\n'

    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('good bye')

