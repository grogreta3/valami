def hanyadik():
    prim=0
    d=10
    szam=2
    oszto=2
    while prim==x:
        for i in range(oszto,0,-1):
            if szam%oszto==0 and oszto==szam:
                prim+=1
                oszto+=1
            elif oszto!=0:
                oszto+=1
                szam+=1
    return szam



print(hanyadik())

