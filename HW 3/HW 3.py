#Создайте класс для хранения комплексных чисел с инициализатором.
#Реализуйте методы, позволяющие представлять комплексное число в экспоненциальной форме.
#Добавьте функции, позволяющие складывать, вычитать, умножать и делить два комплексных числа, 
#результатом работы которых будет новое комплексное число (именно функции, не методы, перегружать операторы тоже не надо).
import math
import numpy as np
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a #Re(z)
        self.b = b #Im(z)

    def __str__(self):
        r = np.round(np.sqrt(self.a**2 + self.b**2), 2) #С точностью до двух знаков после запятой
        phi = np.round(math.atan(self.b/self.a), 2) #С точностью до двух знаков после запятой
        return f'z = {self.a} + {self.b} * i = {r}*exp({phi}*i)' #Вывод алгебраической и экспоненциальной формы
        
    def __add__(self, other): #Сумма
        print(f'Сумма z1 и z2 равна:')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'
    
    def __sub__(self, other): #Разность
        print(f'Разность z1 и z2 равна:')
        return f'z = {self.a - other.a} + {self.b - other.b} * i'

    def __mul__(self, other): #Произведение
        print(f'Произведение z1 и z2 равно:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * i'
    
    def  __truediv__(self, other): #Частное
        x = other.a**2 + other.b**2
        print(f'Частное z1 и z2 равно:')
        return f'z = {(self.a * other.a + (self.b * other.b))/x} + {(self.b * other.a - self.a * other.b)/x} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1) #Output: z = 1 + -2 * i = 2.24*exp(-1.11*i)
print(z_1 + z_2) #Output: Сумма z1 и z2 равна: z = 4 + 2 * i
print(z_1 - z_2) #Output: Разность z1 и z2 равна: z = -2 + -6 * i
print(z_1 * z_2) #Output: Произведение z1 и z2 равно: z = 11 + -2 * i
print(z_1 / z_2) #Output: Частное z1 и z2 равно: z = -0.2 + -0.4 * i
