def displayInventory(inventory):
    print('Inventory')
    totalitems = 0
    for k,v in inventory.items():
        print(v,k)
        totalitems += v
    print('Total number of Items:',totalitems)

def addToInventory(inventory,loot):
    for item in loot:
        inventory[item]=inventory.get(item,0)+1
    return inventory

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print('-'*30)
print('Before Loot:')
print('-'*30)
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print('-'*30)
print('After Loot:')
print('-'*30)
displayInventory(inv)