#help(isinstance)
def calculate_structure_sum(*data_structure):
    calculate_sum = 0.0
    len_data = len(data_structure)
    for i in range(len_data):
        current_item = data_structure[i]
        if isinstance(current_item,(int,float)):
            calculate_sum += float(current_item)
        elif isinstance(current_item,(str)):
            calculate_sum += len(current_item)
        elif isinstance(current_item,(dict)):
            calculate_sum += calculate_structure_sum(*current_item.items())
        else:
            calculate_sum += calculate_structure_sum(*current_item)
    return calculate_sum

data_structure = [
[1, 2, 3.3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)