with open("names2.txt","r") as name:
    names=[name.strip() for name in name.readlines()]
print(names)