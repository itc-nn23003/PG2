def main():
    my_items = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
    display_inventory(my_items)

def display_inventory(inventory):
    print("持ち物リスト:")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        item_total += value
    print("アイテム総数: " + str(item_total))

main()


