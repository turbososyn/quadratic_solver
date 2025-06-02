import sys
import argparse
from src.my_quadratic_solver.solver import solve

def main_interactive():
    print("Програма для розв'язання квадратного рівняння ax^2 + bx + c = 0")
    print("Будь ласка, введіть коефіцієнти.")
    try:
        a = float(input("Введіть коефіцієнт a: "))
        b = float(input("Введіть коефіцієнт b: "))
        c = float(input("Введіть коефіцієнт c: "))
    except ValueError:
        print("\nПомилка: Введено некоректне число. Будь ласка, введіть числові значення.")
        sys.exit(1)
    return a, b, c

def format_roots_uk(result):
    if result['type'] == 'not_quadratic':
        return "Це не квадратне рівняння, оскільки коефіцієнт 'a' дорівнює 0."
    elif result['type'] == 'two_real':
        return f"x₁ = {result['roots'][0]}, x₂ = {result['roots'][1]} (Δ = {result['delta']})"
    elif result['type'] == 'one_real':
        return f"x = {result['roots'][0]} (Δ = {result['delta']})"
    elif result['type'] == 'two_complex':
         return f"x₁ = {result['roots'][0]}, x₂ = {result['roots'][1]} (Δ = {result['delta']})"
    else:
         return "Сталася невідома помилка при розв'язанні."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Розв'язувач квадратного рівняння ax^2 + bx + c = 0.",
        epilog="Приклад неінтерактивного запуску: python main.py -a 1 -b -3 -c 2"
    )
    parser.add_argument('-a', type=float, help='Коефіцієнт a')
    parser.add_argument('-b', type=float, help='Коефіцієнт b')
    parser.add_argument('-c', type=float, help='Коефіцієнт c')

    args = parser.parse_args()

    if args.a is not None and args.b is not None and args.c is not None:
        a, b, c = args.a, args.b, args.c
        print(f"Розв'язання для a={a}, b={b}, c={c}:")
        result = solve(a, b, c)
        print(format_roots_uk(result))
    else:
        a, b, c = main_interactive()
        result = solve(a, b, c)
        print("-" * 20)
        if result['type'] == 'not_quadratic':
            print("Це не квадратне рівняння, оскільки коефіцієнт 'a' дорівнює 0.")
        elif result['type'] == 'two_real':
            print(f"Дискримінант (Δ) = {result['delta']}")
            x1, x2 = result['roots']
            print("Рівняння має два різних дійсних корені:")
            print(f"x₁ = {x1}")
            print(f"x₂ = {x2}")
        elif result['type'] == 'one_real':
            print(f"Дискримінант (Δ) = {result['delta']}")
            x = result['roots'][0]
            print("Рівняння має один дійсний корінь (або два рівних):")
            print(f"x = {x}")
        elif result['type'] == 'two_complex':
             print(f"Дискримінант (Δ) = {result['delta']}")
             x1, x2 = result['roots']
             print("Рівняння має два комплексних корені:")
             print(f"x₁ = {x1}")
             print(f"x₂ = {x2}")
        else:
            print("Сталася невідома помилка при розв'язанні.")
        print("-" * 20)