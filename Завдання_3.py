 try:
    numbers_str = input("Введіть числа через кому: ")  # приклад: 1, 2, 3
    str_list = numbers_str.split(',')
    numbers = [float(num.strip()) for num in str_list]
    average = sum(numbers) / len(numbers)
    print("Середнє значення:", average)
except ValueError:
    print("Помилка: У списку є некоректне число.")
