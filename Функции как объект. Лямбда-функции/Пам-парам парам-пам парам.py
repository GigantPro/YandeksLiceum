line = input().lower()
lines = line.split()
lst = [sum([x in 'ыяиаюоэуе' for x in lin]) for lin in lines]
 
if len(set(lst)) == 1:
    res = "Парам пам-пам"  
else: res = "Пам парам"
print(res)
