years = int(input("Введите год в котором нашща команда рассчитает дни: "))


massiv = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if years % 400 == 0:
    massiv = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if years % 100 != 0:
    if years % 4 == 0:
        massiv = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def CalculateDaysinYears(massiv):
    result: int = 0
    mounthcount: int = 0

    while mounthcount < 12:
        while massiv[mounthcount] > 0:
            result += massiv[mounthcount] // 10
            result += massiv[mounthcount] % 10
            massiv[mounthcount] -= 1
        mounthcount += 1
    return result

print(CalculateDaysinYears(massiv))