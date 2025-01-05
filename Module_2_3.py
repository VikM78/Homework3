my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i_count = 0
len_my_list = len(my_list)
while i_count < len_my_list:
    current_value = my_list[i_count]
    i_count += 1
    if current_value > 0:
        print(f"{current_value}")
    elif current_value == 0:
        continue
    else:
        break
