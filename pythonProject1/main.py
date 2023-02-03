def YearCounter(year, mass):
    result=0
    i=0
    while i<12:
        while mass[i]>0:
            result += mass[i]//10 + mass[i]%10 
            mass[i]-=1
        i+=1
    return result

f = int(input("Введите год: "))
mass = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (f%4==0):
    mass = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(YearCounter(f, mass))