def reverse_string(s):
    a, b = 0, len(s) - 1

    while a < b:
        s[a], s[b] = s[b], s[a]
        a += 1
        b -= 1
    return s
    
s = ["H","a","n","n","a","h"]
print(reverse_string(s))