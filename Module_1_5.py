immutable_var = "String1", 5.6, 25, [55.5, 56, 3.25], True
print("Задан кортеж: ",immutable_var)

#immutable_var[0] = 123
# код в строке выше вызовет ошибку, т.к. неизменяемые
# элементы кортежа изменить нельзя

len_immutable_var = len(immutable_var)
print(f"Количество элементов в кортеже: {len_immutable_var}")

count = 0
for item in immutable_var:
    if type(item)==list:
        print(f"Элемент кортежа с индексом {count} - список\n"
              f"{immutable_var[count]}\n"
              f"Список внутри кортежа можно изменить\n")
    count +=1

mutable_var = ["String1", 5.6, 25, [55.5, 56, 3.25], True]
print(F"А теперь создали список с такими же элементами\n"
      F"Список: {mutable_var}")
len_mutable_var = len(mutable_var)
index_for_modified = -1
error_index = False
while not (index_for_modified in  range(len_mutable_var)):
    while error_index:
        next_command = input("Желаете продолжить?, да/нет: ").lower()
        if next_command == "нет":
            raise SystemExit("Выполнение прервано пользователем")
        elif next_command == "да":
            error_index = False
    index_for_modified = (input(f"Введите индекс изменяемого элемента списка\n"
        f"(от 0 до {len_mutable_var-1}): "))
    if len(index_for_modified)>0:
        if index_for_modified.isnumeric():
            index_for_modified = int(index_for_modified)
            if index_for_modified in range(len_mutable_var):
                mutable_var[index_for_modified] = (input(F""
                    F"Введите новый элемент с индексом {index_for_modified}: "))
                print(f"Измененный список:\n{mutable_var}")
            else:
                print("Введен не верный элемент списка")
                error_index = True
        else:
            print("введено не число")
            error_index = True
    else:
        print("Введена пустая строка")
        error_index = True
