if __name__ == "__main__":
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        num3 = float(input("Введите третье число: "))

        max_num = max(num1, num2, num3)
        print(f"Наибольшее число: {max_num}")

    except ValueError:
        print("Ошибка: Введено некорректное значение.")