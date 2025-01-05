min_list1 = 3
max_list1 = 20
list_1 = list(range(min_list1,max_list1+1))
print(list_1)
chislo1 = 0
while not (chislo1 in list_1):
    chislo1 = int(input(f"Введите число из первой вставки\n"
        f"(от {list_1[0]} до {list_1[len(list_1)-1]}): "))
psw1 = []
psw = ""
for i in range(1,chislo1-1):
    for j in range(i+1,chislo1):
        if i != j:
            if (chislo1%(i + j)) == 0:
                psw1.append(i)
                psw1.append(j)

psw = ''.join([str(elem) for  elem in psw1])
print(f"Искомый пароль: {psw}")