import re
def missingCharacters(s):
    a = re.findall("[A-Z]",s)
    return a

print(missingCharacters("7985interdisciplinary12"))