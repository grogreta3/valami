def Feladat8():
    a = input('Első szó:')     
    b = input('Második szó:')   
    k = ''                      
    for i in a:
        for j in b:             
            if i == j:
                k += j
                break


    if k == '':
        return None
    return k

print(Feladat8())
