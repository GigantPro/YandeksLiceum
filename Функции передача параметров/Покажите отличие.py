a = [1, 345, 856, 110, 25]

print('Значение a до применения метода sort:   ', a)
a.sort()
print('Значение a после применения метода sort:', a)

a = [1, 345, 856, 110, 25]

print('\n\nЗначение a до применения функции sorted:', a)
sorted(a)
print('Значение a после применения функции sorted: ', a)
print('--------------\nВывод: Функция sorted создает новый объект,' + 
      '\nтогда как метод меняет значуние пременной.')
