VOWEL_SOUNDS = ('а','о','у','и','ы','э','е','ё','ю','я', 'a', 'e', 'i', 'u', 'y', 'o' )

def vowel_count(string):
    vowels = 0
    for i in range(len(string)):
        if string[i].lower() in VOWEL_SOUNDS:
            vowels += 1
    return vowels
