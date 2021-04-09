#1
# Создаем словарь
smart = {'model': " MacBook_Air",
         'year': 2020,
         'color': "Space Grey",
         'screen_size': 13.3,
         'storege': 512,
         'price': 1380}
print("smart:", smart)
print("smart_id:", id(smart))

print("="*100)
# Меняем местами первое и последнее значение
first = list(smart.items())[0]
last = list(smart.items())[-1]
smart[first[0]], smart[last[0]] = last[1], first[1]
print("s:", smart)
print("s_id:", id(smart))

# Удаляем второй элемент словаря
print("="*100)
del smart["year"]
# smart.pop('year')
print("smart:", smart)


# Добавляем ключ в конец словаря
print("="*100)
smart["new_key"] = "new_value"
print("new_smart:", smart)
print("new_smart_id:", id(smart))


#2
print("="*100)
student = {"name": "Emma",
           "class": 9,
           "marks": 75}
print(student["marks"])

#3
print("="*100)
p = {"name": "Mike",
     "salary": 8000}
print(p.get("age"))

#4
# Вывести значение "d"
print("="*100)
sample = {"1": ["a", "b"], "2": ["c", "d"]}
print("sample:", sample["2"] [1])

#5
# dict_ = ["Украина": "Киев", "Япония": "Токио", "Беларусь": "Минск"]
print("="*100)
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
d = {dict(a.split('-')[::-1] for a in list_1).get(n): n for n in list_2}
print("dict:", d)



#6
print("="*100)
dict_ = {"A": "5", "B": "&", "C": "#", "D": "21", "E": "s", "F": "к", "G": "vg", "H": "3", "I": "*", "J": "6", "K": ",",
         "L": "b", "M": "%", "N": "1", "O": "$", "P": "4", "Q": "nj", "R": "f", "S": "7", "T": "a", "U": "6", "V": "@d",
         "W": "/.", "X": "03", "Y": "822", "Z": "ed", "a": "dfa", "b": "123", "c": "te", "d": "55", "e": "#@", "f": "324",
         "g": "fas", "h": "kjo", "i": "jnn", "j": "812", "k": "00", "l": "hhb", "m": "po", "n": "33", "o": "765",
         "p": "gaf","q": "89", "r": "675", "s": "*bg", "t": "ypi", "u": "770", "v": "not", "w": "$#)", "x": "!!#",
         "y": ">/h", "z": "546", " ": "_", "+": "^", "-": "Y%", ",": "43", "=": "ga", ".": "de", ":": "665", "!": "90",
         "?": "lk", "@": "49",
         }
word = input("Введите загаданное слов ")
list_shifr = []
print(list(word))
for i in list(word):
    list_shifr.append(dict_[i])
    print(i, dict_[i])
print(list_shifr)
str_shifr = ""
for k in list_shifr:
    str_shifr += k
print(str_shifr)

list_d_shifr = []
for i in list_shifr:
    for key, val in dict_.items():
        if i == val:
            list_d_shifr.append(key)
print(list_d_shifr)


#7
# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
print("="*100)
dict_1 = {a: a ** 3 for a in range(1, 11)}
print("dict_1:", dict_1)

#8
# Создайте словарь из строки: в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
print("="*100)
my_srt = 'vacation'
dict_str = {k: my_srt.count(k) for k in my_srt}
print("dict_str:", dict_str)