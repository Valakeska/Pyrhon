first_operation = True
print("Введите кол-во действий?")
count_operation_read =input()
count_operation = int(count_operation_read)
while count_operation>0:
        print("Выберите действие:\n1) Сложение 2) Вычитание 3) Умножение \n4) Деление 5) Возведение в степень")
        operations = input()
        if first_operation==True:
            number_one = float(input("Введите первое число: "))
            number_two = float(input("Введите второе число:"))
        else:
            number_two = float(input("Введите второе число: "))
        operation = int(operations)
        if operation==1:
            number_one = number_one+number_two
            first_operation = False
            print(f"Ответ: {number_one}")
            count_operation-=1
        elif operation==2:
            number_one = number_one-number_two
            first_operation = False
            print(f"Ответ: {number_one}")
            count_operation-=1
        elif operation==3:
            number_one *=number_two
            first_operation = False
            print(f"Ответ: {number_one}")
            count_operation-=1
        elif operation==4:
            if number_two==0:
                print("Деление на ноль невозможно")
            else:
                number_one = number_one/number_two
                first_operation = False
                print(f"Ответ: {number_one}")
                count_operation-=1
        elif operation==5:
            number_one = number_one**number_two
            first_operation = False
            print(f"Ответ: {number_one}")
            count_operation-=1