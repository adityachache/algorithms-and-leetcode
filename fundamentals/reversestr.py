# Reversing a given string 
def revstr_iterative(s):
    emptystr = ''
    temp = [x for x in s]
    ptr1 = 0
    ptr2 = len(temp)-1
    while ptr1<ptr2:
        temp[ptr1],temp[ptr2] = temp[ptr2],temp[ptr1]
        ptr1 += 1
        ptr2 -= 1
    for word in temp:
        emptystr = emptystr + word
    return emptystr.strip()
print(revstr_iterative("my string is "))


# Reversing a string recursive
def revstr_recursive(s):
    if len(s) == 0:
        return s
    else:
        return revstr_recursive(s[1:]) + s[0]
#print(revstr_recursive("my str"))
 