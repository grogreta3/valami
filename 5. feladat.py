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




   # elif li[i]>li[i+1] and li[i]>li[0]:
    #    new_li2=[li[0]]
        
   #     if len(new_li)>len(new_li2):
   #         print(new_li)
    #    else:
    #        print(nem_li2)


