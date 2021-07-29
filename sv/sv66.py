# a = 15
# b = 10
# c = a + b
# print(c)

# var1 = int(input("Введите число"))
# var2 = input("Введите текст")
# var3 = input("Ведите еще текст")
# var4 = int(input("Введите еще число"))
# print(f"Вот певое число{var1},вот второе число{var4},и текст {var2} {var3}")

# sec = int(input("Введите количество секунд"))
# h = sec // 3600
# m = sec // 60
# print("{}:{}:{}".format(h,m,sec))

# a = 15
# b = 10
# c = a + b
# print(c)

# var1 = int(input("Введите число"))
# var2 = input("Введите текст")
# var3 = input("Ведите еще текст")
# var4 = int(input("Введите еще число"))
# print(f"Вот певое число{var1},вот второе число{var4},и текст {var2} {var3}")

# sec = int(input("Введите количество секунд"))
# h = sec // 3600
# m = sec // 60
# print("{}:{}:{}".format(h,m,sec))


# n = int(input("Введите чило>>>"))
# nn = int(f'{n}{n}')
# nnn = int(f"{n}{n}{n}")
# summ = n + nn + nnn
# print(summ)

# num = int(input("Введите число"))
# a = -1
# while num > 10:
#     b = num % 10
#     num //= 10
#     if b > a:
#         a = b
#         print(a)


plus = int(input("Введите сумму выручек>>>"))
minus = int(input("Введите сумму потерь>>>"))
if plus > minus:
    gain = plus - minus
    los = int(gain / plus)
    print(f"Ваша выручка составила{gain}руб, Рентабельность {los}%" )
else:
    loss =  minus - plus
    print(f"Ваш убыток{loss} руб")
people = int(input("Численность людей"))
if plus > minus:
    peplus = int(gain / people)
    print(f"Зарплата одного человека составила {peplus} руб ")