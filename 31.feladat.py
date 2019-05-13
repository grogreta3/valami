n = input("adj meg egy email cimet:")
while n!="0":
    if "@" and "."  in n:
        n=n.split("@")
        if type(n[0][0])!=str and type(n[0][0])!=int:
            print("nem betuvel vagy szammal kezdtel")
            n = input("adj meg egy email cimet:")
    if "@" or "." not in n:
        print("nem jo az email cim")
        n = input("adj meg egy email cimet:")

    else:
        print(True)
        n = input("adj meg egy email cimet:")