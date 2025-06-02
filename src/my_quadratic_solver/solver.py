import math
import cmath

def solve(a, b, c):
    """
    Розв'язує квадратне рівняння ax^2 + bx + c = 0.

    Повертає словник з типом розв'язку та коренями.
    Типи розв'язків:
    - 'not_quadratic': якщо a == 0
    - 'two_real': два різних дійсних корені
    - 'one_real': один дійсний корінь (дискримінант == 0)
    - 'two_complex': два комплексних корені

    Повертає:
        dict: {'type': str, 'roots': list або None}
    """
    if a == 0:
        return {'type': 'not_quadratic', 'roots': None}

    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return {'type': 'two_real', 'roots': [x1, x2], 'delta': delta}
    elif delta == 0:
        x = -b / (2*a)
        return {'type': 'one_real', 'roots': [x], 'delta': delta}
    else:
        x1_complex = (-b - cmath.sqrt(delta)) / (2*a)
        x2_complex = (-b + cmath.sqrt(delta)) / (2*a)
        return {'type': 'two_complex', 'roots': [x1_complex, x2_complex], 'delta': delta}

if __name__ == '__main__':
    print("Це модуль розв'язання. Запустіть main.py для використання.")