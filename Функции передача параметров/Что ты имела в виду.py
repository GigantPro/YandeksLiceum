numbers = [2, 5, 7, 7, 8, 4, 1, 6]  # Создается список
odd, even = [], []  # Создаются 2 пустых списка
for number in numbers:  # Запускается цикл for
    if number % 2 == 0:  # Проверка на четное число
        even.append(number)  # В массив с четными числами 
    else:  # Если не четное
        odd.append(number)  # Добавляем в список с нечетными числами
