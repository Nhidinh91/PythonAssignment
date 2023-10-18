shoppinglist = []

while True:
    shop = input("Please enter a item you want to shop and enter done to finish: ")
    if shop == "done":
        break
    shoppinglist.append(shop)
print("Your shopping list:\n")
for index,item in enumerate(shoppinglist,start=1):
    print(f"{index}: {item}")
remove_item = input("Enter an item ")