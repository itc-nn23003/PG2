def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

def display_inventory(inventory):
    print("持ち物リスト:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print(f"アイテム総数: {item_total}")
inv = {'金貨': 42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
add_to_inventory(inv, dragon_loot)
display_inventory(inv)