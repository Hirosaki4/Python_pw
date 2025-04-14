try:
    num = float(input("Введіть число з плаваючою точкою: "))
    formatted = f"{num:.2f}"  # округлення до 2 знаків після коми
    print("Відформатоване число:", formatted)
except ValueError:
    print("Помилка: Введено нечислове значення.")
