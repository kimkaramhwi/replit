def complex_number_multiply(a, b):
    a, b = a.replace('i', ''), b.replace('i', '')
    a, b = a.split('+'), b.split('+')
    
    return f"{int(a[0])*int(b[0])-(int(a[1])*int(b[1]))}+{int(a[0])*int(b[1])+int(a[1])*int(b[0])}i"

a = '1+3i'
b = '1+-2i'
print(complex_number_multiply(a, b))