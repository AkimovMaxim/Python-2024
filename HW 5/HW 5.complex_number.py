# Доработайте класс комплексного числа из прошлого 
# занятия: переопределите математические 
# операторы (__+, -, /, *, ==__), так, чтобы они
# работали с другими комплексными и со стандартными
# числами. Добейтесь правильной работы с комплексным 
# числом функций `print()`, `abs()`, а также
# реализуйте `getter` и `setter` 
# с использованием декоратора `@property`. Добавьте 
# выбросы исключений при некорректном использовании 
# вашего числа, например: выбросом `ValueError` при вводе 
# некорректных значений в `setter` класса, выбросом своего исключения в 
# случае попытки перевода в экспоненциальную 
# форму, когда это невозможно. Поверх напишите программу 
# калькулятор, принимающую у пользователя два комплексных
# числа и проводящую с ними арифметические операции на
# выбор пользователя. Калькулятор должен уметь ловить и 
# обрабатывать исключения, не роняя программу,
# а объясняя пользователю, что пошло не так.

import math
import numpy as np
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a #Re(z)
        self.b = b #Im(z)

    def __str__(self):
        try:
            r = np.round(np.sqrt(self.a**2 + self.b**2), 2)
            if self.a == 0 and self.b == 0:
                raise ValueError("Невозможно перевести в экспоненциальную форму: оба значения равны нулю.")
            phi = np.round(math.atan(self.b/self.a), 2) 
            return f'z = {self.a} + {self.b} * i = {r} * exp({phi} * i)'
        except Exception as e:
            return str(e)
        
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a + other.a, self.b + other.b)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.a + other, self.b)
        else:
            raise TypeError("Операция сложения возможна только с комплексными и реальными числами.")
    
    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a - other.a, self.b - other.b)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.a - other, self.b)
        else:
            raise TypeError("Операция вычитания возможна только с комплексными и реальными числами.")

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.a * other, self.b * other)
        else:
            raise TypeError("Операция умножения возможна только с комплексными и реальными числами.")
    
    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            x = other.a**2 + other.b**2
            if x == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return ComplexNumber((self.a * other.a + self.b * other.b) / x, (self.b * other.a - self.a * other.b) / x)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return ComplexNumber(self.a / other, self.b / other)
        else:
            raise TypeError("Операция деления возможна только с комплексными и реальными числами.")

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.a == other.a and self.b == other.b
        return False
    
    @property
    def real(self):
        return self.a
    
    @real.setter
    def real(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Действительная часть должна быть числом.")
        self.a = value
    
    @property
    def imag(self):
        return self.b
    
    @imag.setter
    def imag(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Мнимая часть должна быть числом.")
        self.b = value

    def __abs__(self):
        return np.round(np.sqrt(self.a**2 + self.b**2), 2) # Модуль комплексного числа

# Калькулятор для комплексных чисел
def complex_calculator():
    try:
        # Ввод двух комплексных чисел
        a1 = float(input("Введите действительную часть первого числа: "))
        b1 = float(input("Введите мнимую часть первого числа: "))
        z1 = ComplexNumber(a1, b1)
        
        a2 = float(input("Введите действительную часть второго числа: "))
        b2 = float(input("Введите мнимую часть второго числа: "))
        z2 = ComplexNumber(a2, b2)
        
        # Выбор операции
        operation = input("Выберите операцию (+, -, *, /): ")
        
        if operation == "+":
            result = z1 + z2
        elif operation == "-":
            result = z1 - z2
        elif operation == "*":
            result = z1 * z2
        elif operation == "/":
            result = z1 / z2
        else:
            raise ValueError("К сожалению, мы не знаем, как работать с такой операцией...")
        
        print(f"Результат: {result}")
    
    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except ZeroDivisionError as zde:
        print(f"Ошибка: {zde}")
    except TypeError as te:
        print(f"Ошибка типа данных: {te}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
complex_calculator()
