
def simple(x):
	d = 2
	if(x == 2):
		return True
	else:
		if(x % d != 0):
			return True
		else:
			return False
num = int(input("Введите число --> ")) #Воод числа
if(num > 1):
		if(simple(num) == True):
			print(f'Число {num} является простым.')
		else:
			print(f'Число {num} не является простым.')
else: # Если число равно или меньше единицы
	print('Число должно быть больше единицы.')