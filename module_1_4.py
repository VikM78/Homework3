my_string = input("Введите текст: ")
len_string = len(my_string)
print(len_string)
print("Uppercase: ",my_string.upper())
print("lowercase: ",my_string.lower())
print("Без пробелов: ",my_string.replace(" ",""))

#Усложнил задание - вывожу строку "Как в предложении"
my_string2 = my_string[0].upper() + my_string[1:].lower()
print(my_string2)

print("Первый символ строки: ",my_string[0])

print("Последний символ строки: ",my_string[len_string-1:])