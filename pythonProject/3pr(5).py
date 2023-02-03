import random #Импорт случайных чисел
def gen(x):
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # Набор английских букв
	if(x == 1): # Генерация номера старого формата
		return f'{alpha[random.randint(0,25)]}{alpha[random.randint(0,25)]}{alpha[random.randint(0,25)]}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
	else: # Генерация номера нового формата
		return f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{alpha[random.randint(0,25)]}{alpha[random.randint(0,25)]}{alpha[random.randint(0,25)]}'
x = random.randint(1,2)
number = gen(x)
print(f'Новый номерной знак: {number}')