from typing import Any


class ShoppingList:
    def __init__(self):
        self.items = ["Apple", "Banana", "Milk", "Carrot"]

    def __getitem__(self, idx):
        return self.items[idx]

    def __len__(self):
        return len(self.items)

shoppinglist = ShoppingList()
print(shoppinglist[0])
print("-----------------------")

for i in shoppinglist:
    print(i)
print("-----------------------")

if "Milk" in shoppinglist:
    print("Milk is also in the list")

print(len(shoppinglist))
