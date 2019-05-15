li=input('adj meg egy szam sort vesszovel elvalasztva:')
li=li.split(',')
new_li=[]
new_li2=[]
n=len(li)-1
for i in range(n):
    if li[i]<li[i+1]:
        new_li.append(li[i])
        print(new_li,new_li2)
    if li[i]>li[i+1]:
        new_li.append(li[i])
        if len(new_li)>len(new_li2):
            new_li2=new_li
            new_li=[li[0]]
            print(new_li,new_li2)
        else:
            new_li=[li[0]]

if li[-1]>new_li[-1]:
    new_li.append(li[-1])
if len(new_li2)==0:
    print(new_li,len(new_li))
else:
    print(new_li2, len(new_li2))

