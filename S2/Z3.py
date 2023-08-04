# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.



from fractions import Fraction
import math

def sum_Fraction(number_frac_1, number_frac_2):
    sum_frac = [int(number_frac_1[0]) * int(number_frac_2[1]) \
                       + int(number_frac_2[0]) * int(number_frac_1[1]),
                int(number_frac_1[1]) * int(number_frac_2[1])]
    nod = math.gcd(sum_frac[0], sum_frac[1])
    sum_frac = [int(sum_frac[0] / nod), int(sum_frac[1] / nod)]
    print('Cумма дробей = ', sum_frac[0], '/', sum_frac[1])

def mult_Fraction(number_frac_1, number_frac_2):
    mult_frac = [int(number_frac_1[0]) * int(number_frac_2[0]),
                 int(number_frac_1[1]) * int(number_frac_2[1])]
    nod = math.gcd(mult_frac[0], mult_frac[1])
    mult_frac = [int(mult_frac[0] / nod), int(mult_frac[1] / nod)]
    print('Произведение дробей = ', mult_frac[0], '/', mult_frac[1])

def Main():
    number_frac_1 = str(input('Введите первое число вида a/b - ')).split('/')
    number_frac_2 = str(input('Введите второе число вида a/b - ')).split('/')
    sum_Fraction(number_frac_1, number_frac_2)
    mult_Fraction(number_frac_1, number_frac_2)
    print('Проверка:')
    print(f"{number_frac_1} + {number_frac_2} = {Fraction(int(number_frac_1[0]), int(number_frac_1[1])) + Fraction(int(number_frac_2[0]), int(number_frac_2[1]))}")
    print(f"{number_frac_1} * {number_frac_2} = {Fraction(int(number_frac_1[0]), int(number_frac_1[1])) * Fraction(int(number_frac_2[0]), int(number_frac_2[1]))}")


Main()