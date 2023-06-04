number = input("Введите шестизначное число: ")

# Проверяем длину строки
if len(number) != 6:
    print("Ошибка: Введено некорректное число!")
else:
    # Суммируем первые три цифры и вторые три цифры
    sum1 = int(number[0]) + int(number[1]) + int(number[2])
    sum2 = int(number[3]) + int(number[4]) + int(number[5])

    # Проверяем условие счастливого числа
    if sum1 == sum2:
        print("Введенное число является счастливым!")
    else:
        print("Введенное число не является счастливым!")

number = input("Введите шестизначное число: ")

# Проверяем длину строки
if len(number) != 6:
    print("Ошибка: Введено некорректное число!")
else:
    # Получаем цифры числа
    digit1 = number[0]
    digit2 = number[1]
    digit3 = number[2]
    digit4 = number[3]
    digit5 = number[4]
    digit6 = number[5]

    # Формируем новое число с поменянными цифрами
    new_number = digit1 + digit5 + digit3 + digit4 + digit2 + digit6

    print("Исходное число:", number)
    print("Модифицированное число:", new_number)


month = int(input("Введите номер месяца (от 1 до 12): "))

if month == 1 or month == 2 or month == 12:
    season = "Winter"
elif month >= 3 and month <= 5:
    season = "Spring"
elif month >= 6 and month <= 8:
    season = "Summer"
elif month >= 9 and month <= 11:
    season = "Autumn"
else:
    print("Ошибка: Введено некорректное значение!")
    exit()

print("Сезон:", season)
