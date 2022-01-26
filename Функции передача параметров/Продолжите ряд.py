def continue_fibonacci_sequence(sequence, n):  # определение функции
    for i in range(n):  # цикл фор
        next_element = sequence[-1] + sequence[-2]  # следующий элемент = сумме предыдущих
        sequence.append(next_element)  # добавляется в массив с элементами
