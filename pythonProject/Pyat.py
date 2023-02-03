import colorama
from colorama import Fore, Back, Style

# Работа с датой и временем
import time, datetime

# Работа с json файлами
import json

from web3 import Web3

from web3.middleware import geth_poa_middleware

#Cоздаем экзмемпляр подключения
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Считываем abi смарт-контракта и помещаем данные из файла в переменную abi
with open("abi.txt", "r") as file:
    abi = json.loads(file.read())

# Адрес смарт-контракта
address = "0xd8b934580fcE35a11B58C6D73aDeE468a2833fa8"

# Указываем что это адрес контракта
contract_address = Web3.toChecksumAddress(address)

web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Создаем объект контракта
contract = web3.eth.contract(address=address, abi=abi)


def Add_create():
        print("Заполните цену недвижимости: ")
        price = int(input())
        print("Заполните информацию о недвижимости: ")
        info = input()
        print("Заполните ссылку на изображение: ")
        picture = input()
        print("Заполните номер телефона: ")
        phone = input()
        print("Заполните индекс дома: ")
        index = int(input())
        fx = contract.functions.ViewPlace(index).call()
        if web3.eth.defaultAccount == fx[0]:
            if price > 0:
                tx = contract.functions.AdCreate(price, info, picture, phone, index).transact()
                main()
            else:
                print(Fore.RED + "Цена должна быть выше нуля")
                print(Style.RESET_ALL)
                main()
        else:
            print(Fore.RED + "Вы не являетесь владелецем")
            print(Style.RESET_ALL)
            main()

def Add_appartment():
        print("Заполните площадь: ")
        square = int(input())
        print("Заполните тип недвижимости: ")
        type = int(input())
        if square > 0:
            if type >= 0 and type <5:
                tx = contract.functions.PlaceCreate(square, type).transact()
                main()
            else:
                print(Fore.RED + "Всего 4 типа недвижимости выберите от 0 до 4")
                print(Style.RESET_ALL)
                main()
        else:
            print(Fore.RED + "Площадь должна быть больше нуля")
            print(Style.RESET_ALL)
            main()

def viewadd():
        print("Заполните индекс объявления: ")
        index = int(input())
        fx = contract.functions.ViewAd(index).call()
        print(f"Владелец: {fx[0]}")
        print(f"Цена: {fx[1]}")
        print(f"Индекс дома: {fx[2]}")
        print(f"ИНформация про дом: {fx[3]}")
        print(f"Картинка: {fx[4]}")
        print(f"Номер телефона: {fx[5]}")
        print(f"Статус: {fx[6]}")
        main()

def viewplace():
        print("Заполните индекс дома: ")
        index = int(input())
        tx = contract.functions.ViewPlace(index).call()
        print(f"Владелец: {tx[0]}")
        print(f"Площадь: {tx[1]}")
        print(f"Тип дома: {tx[2]}")
        main()

def Buy_Place():
        print("Заполните индекс объявления: ")
        adsindex = int(input())
        fx = contract.functions.ViewAd(adsindex).call()
        if web3.eth.defaultAccount == fx[0]:
            print("Вы являетесь владельцем!!!")
            print(Style.RESET_ALL)
            main()
        else:
            if fx[6] == False:
                print("Статус объявления не активен!!!")
                print(Style.RESET_ALL)
                main()
            else:
                if web3.eth.getBalance(web3.eth.defaultAccount) >= (fx[1]+10**18):
                    dx = contract.functions.BuyPlace(adsindex).transact({f"from": f"{web3.eth.defaultAccount}", "value": int(fx[1]+10**18)})
                    main()
                else:
                    print("Статус объявления не активен!!!")
                    print(Style.RESET_ALL)
                    main()

def main():
        print("Выберите одну из функиций:"
            "\n1 - Создать новое объявление"
            "\n2 - Создать новую недвижимость"
            "\n3 - Купить недвижимость"
            "\n4 - Посмотреть недвижимость"
            "\n5 - Посмотреть объявление")
        action = int(input())
        match(action):
            case 1:
                Add_create()
            case 2:
                Add_appartment()
            case 3:
                Buy_Place()
            case 4:
                viewplace()
            case 5:
                viewadd()
            case _:
                print("Выбранна неверная операцию")
                main()


if __name__ == '__main__':
        print("Заполните ваш адресс: ")
        web3.eth.defaultAccount = input()
        print("Агентство недвижимости")
        main()
