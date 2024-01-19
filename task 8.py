

lst = ["sardor", "sarvar"]
ln = len(lst)

for name in lst:
    if ln == 0:
        print("no online")

    elif ln == 1:
        print(lst[0] + "online")

    elif ln == 2:
        print(f"{lst[0]} and {lst[1]}" + " online")