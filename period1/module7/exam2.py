names = set()
while True:
    name = input("Enter a name:\n")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
for name in names:
    print(name)