first  = int(input('Введите 1е число: '))
second = int(input('Введите 2е число: '))
third  = int(input('Введите 3е число: '))
if first == second == third:
    tmp_result = 3
elif first == second or first == third or second == third:
    tmp_result = 2
else:
    tmp_result = 0
print(tmp_result)
