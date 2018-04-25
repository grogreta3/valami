def prim():
    oszto=2
    if x==1:
        return "nem prim"
    else:
        for i in range(x):
            if x%oszto==0 and oszto==x:
                return "prim"
            elif x%oszto !=0:
                oszto+=1
            else:
                return "nem prim"


def prim_e(d):
    sz=0
    for i in range(d*3):
        if sz == d:
            return i
        elif prim(i)==True:
            sz+=1
