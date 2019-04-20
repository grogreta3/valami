def lista(li):
    uj_li=[]
    i=0
    while i!=len(li)-1:
        if li[i]<li[i+1]:
            uj_li.append(li[i])
            i+=1
        if li[i]>li[i+1]:
            break
    if li[i]>li[i-1]:
        uj_li.append(li[i])

    return uj_li,len(uj_li)

li=input('adj meg egy listát vesszővel elválasztva:')
li=li.split(',')
uj_li=[]
for i in li:
    i=int(i)
    uj_li.append(i)
print(uj_li)
print(lista(uj_li))
print(li)
