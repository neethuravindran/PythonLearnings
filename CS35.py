itemlist = input("Enter list of items ")
find_elem = input("Enter the elements which needs to find>>> ")

itemlistel = str(itemlist).split(",")

elimspace = [name.strip() for name in itemlistel]

if find_elem in elimspace:
    print(f"{find_elem} is present in given list at position {elimspace.index(find_elem)+1}")
else:
    print(f"{find_elem} is not present in given list")