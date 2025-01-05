calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    tuple_1 = []
    tuple_1.append(len(string))
    tuple_1.append(string.upper())
    tuple_1.append(string.lower())
    tuple_1 = tuple(tuple_1)
    count_calls()
    return tuple_1

def is_contains (string, list_to_search):
    is_contains_ = False
    string_to_find = ''
    string.lower()
    for i in range(len(list_to_search)):
        string_to_find = str(list_to_search[i])
        string_to_find.lower()
        if string_to_find in string:
            is_contains_ = True
    count_calls()
    return is_contains_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)