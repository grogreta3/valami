def lista(li):
    uj_li=[]
    idx=0
    s=0
    while idx!=(len(li)-1):
    	if li[idx]<li[idx+1]:
    		uj_li.append(li[idx])
    		s=uj_li[idx]
    	idx+=1
    	
    	if li[idx]>li[idx+1]:
    		idx+=1
    return uj_li,len(uj_li)
    		

li=input('adj meg egy listát vesszővel elválasztva:')
li=li.split(',')
uj_li=[]
for i in li:
    i=int(i)
    uj_li.append(i)
print(uj_li)
print(lista(uj_li))
