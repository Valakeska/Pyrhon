import datetime
users = {
"Менендес Дмитрий Владиславович": {"dateBirth": datetime.datetime(2002, 10, 10), "emailAddress": " menendez@hmail.com "},
"Волошин Владислав Викторович": {"dateBirth": datetime.datetime(1945, 7, 5), "emailAddress": " vvvoloshin@hmail.com "},
"Якупов Амир Альбертович": {"dateBirth": datetime.datetime(2016, 3, 7), "emailAddress": " nikolasAmir@hmail.com "},
"Грибков Матвей Андреевич": {"dateBirth": datetime.datetime(1974, 1, 6), "emailAddress": " MaslinaGrib@hmail.com "},
"Димидов Артем Русланович": {"dateBirth": datetime.datetime(2012, 12, 12), "emailAddress": " DimArRy@hmail.com "},
}
Date = (input("Введите дату выпуска (ГГГГ/ММ/ДД) \n"))
time = datetime.datetime.strptime(Date, "%Y/%m/%d")
for key, value in users.items():
    if value["dateBirth"] > time:
        print(key)