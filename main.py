import sys
from my_quadratic_solver.solver import solve

def main():
    """
    Основна функція для взаємодії з користувачем та виведення результатів.
    """
    print("Програма для розв'язання квадратного рівняння ax^2 + bx + c = 0")
    print("Будь ласка, введіть коефіцієнти.")

    try:
        
        a = float(input("Введіть коефіцієнт a: "))
        b = float(input("Введіть коефіцієнт b: "))
        c = float(input("Введіть коефіцієнт c: "))
    except ValueError:
        print("\nПомилка: Введено некоректне число. Будь ласка, введіть числові значення.")
        sys.exit(1) 

    result = solve(a, b, c)

    print("-" * 20)

    if result['type'] == 'not_quadratic':
        print("Це не квадратне рівняння, оскільки коефіцієнт 'a' дорівнює 0.")
    elif result['type'] == 'two_real':
        delta = result['delta']
        x1, x2 = result['roots']
        print(f"Дискримінант (Δ) = {delta}")
        print("Рівняння має два різних дійсних корені:")
        print(f"x₁ = {x1}")
        print(f"x₂ = {x2}")
    elif result['type'] == 'one_real':
        delta = result['delta']
        x = result['roots'][0]
        print(f"Дискримінант (Δ) = {delta}")
        print("Рівняння має один дійсний корінь (або два рівних):")
        print(f"x = {x}")
    elif result['type'] == 'two_complex':
        delta = result['delta']
        x1, x2 = result['roots']
        print(f"Дискримінант (Δ) = {delta}")
        print("Рівняння має два комплексних корені:")
        print(f"x₁ = {x1}")
        print(f"x₂ = {x2}")
    else:
        print("Сталася невідома помилка при розв'язанні.")

    print("-" * 20)

if __name__ == "__main__":
    main()