# Максимум в списке
def find_max(mylist):
    len_list = len(mylist)
    max_in_list = mylist[0]
    if len_list > 1:
        for i in range(len_list):
            if max_in_list < mylist[i]:
                max_in_list = mylist[i]
    return max_in_list

# Подсчет четных чисел в списке
def count_even(mylist):
    counter = 0
    for i in mylist:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter

# Уникальный список
def unique(mylist):
    mylist_new = []
    for i in mylist:
        if i not in mylist_new:
            mylist_new.append(i)
    return mylist_new


mylist = [89, 96, 74, 20, 101, 0, 2, 5, 2, 74]
print(f"Максимальный элемент списка {mylist}: {find_max(mylist)}")
print(f"Количество четных элементов списка {mylist}: {count_even(mylist)}")
print(f"уникальный список из списка {mylist}: {unique(mylist)}")


