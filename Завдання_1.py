try:
    user_input = input("Введіть число: ")
    number = float(user_input) if '.' in user_input else int(user_input)
    result = number * 2  # наприклад, множимо на 2
    print("Результат (у вигляді рядка):", str(result))
except ValueError:
    print("Помилка: Введене значення не є числом.")
