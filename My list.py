def reverseWords(word):
    rev = ""
    for i in range(1, len(word)):
        rev = rev + word[-i]
    rev = rev + word [0]
    return rev

def reverse(target):
    rev = []
    for i in range(1,len(target)+1):
        rev.append(target[-i])
    return rev
print(reverse(["Dylan", "Cole", "Caleb", "Bruh"]))
