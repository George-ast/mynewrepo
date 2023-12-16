"""Сount_vowels.
"""


def count_vowels(text):
    vowels = 'aeiouAEIOU'
    vowels_count = {vowel: text.count(vowel) for vowel in vowels}
    return vowels_count

poem_text = """I wandered lonely as a cloud.

That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.
Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance.
"""
result = count_vowels(poem_text)

print(f' | {"Vowel":^5} | {"Count":^5} | ')
print('-' * 19)

for vowel, count in result.items():
    print(f' | {vowel:^5} | {count:^5} | ')
print('-' * 19)

def change_string(inputstring):
    vowels = {
        'a': 'à',
        'e': 'é',
        'i': 'í',
        'o': 'ó',
        'u': 'ú',
        'A': 'À',
        'E': 'É',
        'I': 'Í',
        'O': 'Ó',
        'U': 'Ú'
    }
    for key in vowels.keys():
        inputstring = inputstring.replace(key, vowels[key])
    print(inputstring)

count_vowels(poem_text)
change_string(poem_text)
