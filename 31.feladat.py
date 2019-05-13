#Íef emailolvaso(n):




n=input("adj meg egy email cimet:")
while n!=0:
    if "@" or "." not in n:
        print(False)
        n=input("adj meg egy email cimet:")
    if "@" or "." not in n:
        n=n.split("@")
        for i in n[0]:
            if n[0][0].style!=str or n[0][0].style!=int:
                print(False)
                n = input("adj meg egy email cimet:")
    else:






        print(True)




#email=input("adj meg egy email cimet:")
#email1=email.split("@")
#email2=email.split(".")
#print(email1,email2)