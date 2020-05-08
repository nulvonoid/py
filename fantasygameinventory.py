inv = {'rope' : 1, 'gold coin' : 42}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display(inventory):
    print ('Inventory : ')
    total = 0
    for k,v in inv.items():
        print (str(v) +' '+ k)
        total += v
    print('total: '+  str(total))


def addInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inv.setdefault(addedItems[i],0)
        inv[addedItems[i]] = inv[addedItems[i]] + 1
    return inv 

inv = addInventory(inv,dragonLoot)
display(inv)

