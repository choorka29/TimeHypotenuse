import time

def log_calc_hypotenuse(func):
    def timer(a, b):
        start_time = time.time()
        result = func(a, b)
        end_time = time.time()

        print(f"Время начала работы функции: {start_time}")
        print(f"Стороны прямоугольного треугольника: a = {a}, b = {b}")
        print(f"Результат вычисления: {result}")
        print(f"Время окончания работы функции: {end_time}")
        print(f"Время выполнения функции: {end_time - start_time} сек")

        return result
    return timer

@log_calc_hypotenuse
def calc_hypotenuse(a, b):
    c = (a**2 + b**2) ** 0.5
    return c

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

hypotenuse = calc_hypotenuse(a, b)
print(f"Длина гипотенузы: {hypotenuse}")