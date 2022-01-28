inp = input().lower().split()
ls = [sum([1 for x in lin if x in 'ыяиаюоэуе']) for lin in inp]
 
if len(set(ls)) == 1:
    res = "Парам пам-пам"  
else: 
    res = "Пам парам"
print(res)
