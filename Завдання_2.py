try:
    a = input("Введіть перше число: ")
    b = input("Введіть друге число: ")

    a_num = float(a) if '.' in a else int(a)
    b_num = float(b) if '.' in b else int(b)

    print(f"Сума: {a_num + b_num}")
    print(f"Різниця: {a_num - b_num}")
    print(f"Добуток: {a_num * b_num}")
    if b_num != 0:
        print(f"Частка: {a_num / b_num}")
    else:
        print("Ділення на нуль неможливе.")
except ValueError:
    print("Помилка: Одне або обидва значення не є числом.")
