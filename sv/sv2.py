# password = input("Введите пороль>>>")
#
# original_password = "correct"
#
# if original_password == password:
#     print("Верно")
# else:
#     print("Неверно")

age = int(input("Введите возраст"))

if age >= 14:
    print("Паспорт можно получить")

    if 20 <= age < 45:
        input("Паспорт можно поменять")
    elif age <1:
       print("Custom")
else:
    print("Паспорт нельзя получить")
