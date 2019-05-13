#Íef emailolvaso(n):

n = input("adj meg egy email cimet:")
while n!="0":
    if "@" and "." not in n:
        print("nem megfelelo az email cim")
        n = input("adj meg egy email cimet:")
    elif "@" and "."  in n:
        n=n.split("@")
        if type(n[0][0])!=str and type(n[0][0])!=int:
            print("nem betuvel vagy szammal kezdtel")
            n = input("adj meg egy email cimet:")
    else:
        print(True)
        n = input("adj meg egy email cimet:")




#email=input("adj meg egy email cimet:")
#email1=email.split("@")
#email2=email.split(".")
#print(email1,email2)