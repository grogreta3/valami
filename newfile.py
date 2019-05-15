li=input('adj meg egy szam sort vesszovel elvalasztva:')
li=li.split(',')
new_li=[li[0]]
new_li2=[li[0]]
idx=0
while idx!=len(li)-1:
    if li[idx]<li[idx+1] and li[idx+1]> new_li[-1]:
        new_li.append(li[idx+1])
        idx+=1
    elif li[idx]>li[idx+1] :
        if li[idx] < new_li[-1]:
            idx += 1
        else:
            if len(new_li)<len(new_li2):
                idx+=1
                new_li=[li[0]]
            else:
                new_li, new_li2 = new_li2, new_li
                new_li.append(li[idx + 1])
                idx+=1






if li[-1]>new_li[-1]:
    new_li.append(li[-1])

print(new_li, len(new_li))
