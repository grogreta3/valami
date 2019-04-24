def lista(li):
    uj_li=[]
    idx=0
    s=0
    for i in range(len(li)-1):
        if li[i]<li[i+1]:
            uj_li.append(li[i])
            idx+=1
            s=li[i]
            print (s)
    if li[idx+2]>s:
        uj_li.append(li[idx+1])

    return uj_li,len(uj_li)




li=input('adj meg egy listát vesszővel elválasztva:')
li=li.split(',')
uj_li=[]
for i in li:
    i=int(i)
    uj_li.append(i)
print(uj_li)
print(lista(uj_li))
