# remove wovels from a string

def remove_vowels(string):
    str = ""
    for i in string:
        i = i.lower()

        if i not in "aeiou":
            str+= i
    return str


print(remove_vowels("apple"))





