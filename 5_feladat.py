def feladat_5():
    
    sum = 0
    while sum != 100:
        x = int(input("Szam:"))
        if sum < 100:
            sum += x
        if sum > 100:
            sum -= x

    return sum


print(feladat_5())
