'''
first = input("Adja meg az első szót! ")
second = input("Adja meg a második szót! ")



kozos=[]
for i in range(0,len(first)):
    for j in range(0,len(second)):
        if first[i] == second[j] :
            kozos.append(second[j])

vegso=""
for i in kozos:
    if i not in vegso:
        vegso+=i

print(vegso)
'''

def Feladat8():
    a = input('Első szó:')      #Bekéri az első szót
    b = input('Második szó:')   #Bekéri a másodikat
    k = ''                      #üres sztring
    for i in a:
        for j in b:             #dupla ciklus, ha egyezést talál beilleszti az üres sztring-be
            if i == j:
                k += j
                break


    if k == '':
        return None
    return k

print(Feladat8())