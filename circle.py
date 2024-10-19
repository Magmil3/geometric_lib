import math


def area(r):
    '''
     //Функция находит площадь круга с переданным радиусом
        Пример вызова функции: 
        input: area(4)
        output: 50,2654//
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    //Функция находит длину окружности с заданным радиусом
        Пример вызова функции:
        input: preimeter(5)
        output: 31,4159//
    '''
    return 2 * math.pi * r