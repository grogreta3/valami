"""
li=input('adj meg egy szam sort vesszovel elvalasztva:')
li=li.split(",")
new_li=[]
idx=0
for i in range(len(li)-1):
    if li[i]<li[i+1]:
        new_li.append(li[i])
        idx+=1


if li[-1]>new_li[-1]:
    new_li.append(li[idx])

print(new_li)
"""

li=input('adj meg egy szam sort vesszovel elvalasztva:')
li=li.split(',')
new_li=[li[0]]
for i in range(len(li)-1):
    i=int(i)
    if li[i]<li[i+1]:
        new_li.append(li[i+1])
    else:
        newli2=[li[0]]
        if li[i]>newli2[j]:
            newli2.append(li[i])

        if len(new_li)<len(newli2):
            new_li=newli2
            newli2=[]
            print(newli2)
print(new_li)








