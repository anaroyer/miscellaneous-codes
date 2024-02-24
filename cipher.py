def rotate(text, key):
    string_text = str(text)
    new_text = ''
    alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if key > 26:
        rotated_key = key - 26
        alphabet_lowercase_rotated = alphabet_lowercase[rotated_key:] + alphabet_lowercase[:rotated_key]
        alphabet_uppercase_rotated = alphabet_uppercase[rotated_key:] + alphabet_uppercase[:rotated_key]
    if key <= 26:
        alphabet_lowercase_rotated = alphabet_lowercase[key:] + alphabet_lowercase[:key]
        alphabet_uppercase_rotated = alphabet_uppercase[key:] + alphabet_uppercase[:key]

    for letter in string_text:
        if letter.islower() is True:
            position = alphabet_lowercase.index(letter)
            new_letter = alphabet_lowercase_rotated[position]
            new_text += new_letter
            continue
        if letter.isupper() is True:
            position = alphabet_uppercase.index(letter)
            new_letter = alphabet_uppercase_rotated[position]
            new_text += new_letter
            continue
        if letter.isspace() is True:
            new_text += ' '
            continue
        if letter.isalpha() is False:
            new_text += letter
            continue
    return new_text