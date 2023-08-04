# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.


BASE = 16
number = int(input('Введите число: '))

bin_number = ''
print(hex(number)[2:])
while number > 0:
    bin_number += str(number%BASE)
    number //= BASE

print(bin_number[::-1])