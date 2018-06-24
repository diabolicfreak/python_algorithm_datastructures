def anagram(s1, s2):
    s1 = list(str(s1).replace(' ', '').lower())
    s2 = list(str(s2).replace(' ', '').lower())
    print(s1, s2)
    for c in s1:
        if c in s2:
            s2.remove(c)
        else:
            return False
    if s2:
        return False
    else:
        return True
        
def anagram1(s1, s2):
    s1 = list(str(s1).replace(' ', '').lower())
    s1 = list(str(s2).replace(' ', '').lower())
    return sorted(s1) == sorted(s2)

def anagram2(s1, s2):
    s1 = list(str(s1).replace(' ', '').lower())
    s1 = list(str(s2).replace(' ', '').lower())

    count = {}

    for c in s1:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    for c in s2:
        if c in count:
            count[c] -= 1
        else:
            count[c] = 1

    for k in count:
        if count[k] != 0:
            return False 
        
    return True
