v=input("adj meg egy email cimet:")

def felhaszn(fel_szo):
    idx=1
    jelek = ['-', '_', '.']
    if fel_szo[0].isalnum()==False or fel_szo[-1].isalnum()==False:
        return 'A felhasznalonev nem helyes'
    for i in fel_szo:
        if fel_szo[idx] not in jelek and fel_szo[idx].isalnum()==False:
            idx+=1
            return 'A felhasznalonev nem helyes'
    else:
        return 'A felhasznalonev jo'


def kisz(ki_szo):
    idx=1
    jelek = ['-', '.']
    if ki_szo[0].isalnum()==False or ki_szo[-1].isalnum()==False:
        return 'A kiszolgalonev nem helyes'
    for i in ki_szo:
        if ki_szo[idx] not in jelek and ki_szo[idx].isalnum()==False:
            idx+=1
            return 'A kiszolgalonev nem helyes'
    else:
        return 'A kiszolgalonev jo'

def tld(tld):
    idx=1
    if tld[0].isalpha() == False or tld[-1].isalpha() == False:
        return 'A tld nem helyes'
    for i in tld:
        if tld[idx].isdigit()==True:
            idx+=1
            return 'A tld nem helyes'

    else:
        return 'A tld helyes'

while v!=0:
    for i in v:
        if "@" and "." in v:
            v=v.split("@")
            felh=v[0]
            v=v[1].split(".")
            kiszol=v[0]
            tldszo=v[1]
            if felhaszn(felh)=="A felhasznalonev jo" and kisz(kiszol)=="A kiszolgalonev jo" and tld(tldszo)=="A tld helyes":
                print("Az email cim jo")
                v=input("adj meg egy uj email cimet")
            else:
                print("Az email cim nem heyles")
                v=input("adj meg egy masik email cimet")
        else:
            print("Az email cim helytelen")
            v = input("adj meg egy masik email cimet")
