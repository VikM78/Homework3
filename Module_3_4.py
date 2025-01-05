def single_root_words(root_word = '', *other_words):
    same_words = []
    lower_root_word = ''
    current_other_word = ''
    for i in range(len(other_words)):
        current_other_word = str(other_words[i]).lower()
        lower_root_word = root_word.lower()
        if (lower_root_word in current_other_word) or (current_other_word in lower_root_word):
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)



