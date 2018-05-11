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
