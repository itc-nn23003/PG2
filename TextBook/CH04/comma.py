def list_to_string(items):
    if not items:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]


spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(spam))

empty_list = []
print(list_to_string(empty_list))
