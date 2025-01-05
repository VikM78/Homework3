count = 0
def get_multiplied_digits(number):
    global count
    str_number = str(number)
    first = int(str_number[0])
    if first == 0:
        if count == 0:
            first = 0
        else:
            first = 1
    if len(str_number) > 1:
        count = 1
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        count = 0
        return first

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
result3 = get_multiplied_digits(0)
print(result3)