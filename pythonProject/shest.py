print("Вводите числа")
N = 3
l = []
m = []
p = []
while N != "":
    N =input()
    if N == "":
        break
    if int(N) > 0:
        l.append(int(N))
    elif int(N) == 0:
        m.append(int(N))
    elif int(N)<0:
        p.append(int(N))
print(p , m , l)