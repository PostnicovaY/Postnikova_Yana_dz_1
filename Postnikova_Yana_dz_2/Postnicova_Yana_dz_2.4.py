#Чтобы найти число в элементах списка:

#1. Проверить с помощью S.isdigit()
#2. Например дано:
a = [5, 'dkfj78df', 9, 8, 'dkfj8']
b = []
for el in a:
    if type(el) == int:
        b.append(el)
    else:
        for c in el:
            import re
            c = re.search(r'\d+\.?\d*',el) #Чисто случайно нашла это выражение в интернете: ищем в строке совпадение с числом плюсуем, если 2 числа рядом
            c = c.group()
            c = int(c)
        b.append(c)

print(b)

#Теперь задача со списком:

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in my_list:
    my_list = el.split(' ')[-1].capitalize()
    print(f"Привет, {my_list}!")

