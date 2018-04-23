from math import pi
def main():
    m = float(input("adja meg a medence magassagat:"))
    alak = input("adja meg a medence alakját(negyzet/kor)")

    if alak == "negyzet":
       h = float(input("adja meg a medence oldalhosszat:"))
       T = h*h
       m = m*0.8

    else:
       r = float(input("adja meg a kor sugarat:"))
       T = pi*r*r

    V = str(m*T)
    print("A szukseges viz mennyisege", V , "mˇ3")



main()