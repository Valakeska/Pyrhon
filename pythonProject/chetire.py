print("Вводите числа, 0 - индикатор окончания")
nums = []
n = 1
while n != 0:
    try:
        n = int(input())
        if n!= 0:
            nums. append(n)
    except:
        print("Некоректный ввод!")
nums.sort()
for i in range(len(nums)):
    print(nums[i])