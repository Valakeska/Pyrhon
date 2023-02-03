
def division(x, y):
	while((x != 0) and (y != 0)):
		if(x>y):
			x = x % y
		else:
			y = y % x
	return x+y
# Ввод чисел пользователем
a = int(input("Введите числитель --> "))
b = int(input("Введите знаменатель --> "))
c = division(a,b) #Переыдача значений в функцию
print("Итоговая дробь: " + str(int(a/c)) + "/" + str(int(b/c))) #Вывод итоговой дроби