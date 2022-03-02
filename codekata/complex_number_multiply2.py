def complex_number_multiply(a, b):
  a1, a2 = map(int, a[:-1].split('+'))
  b1, b2 = map(int, b[:-1].split('+'))
  return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)

a = '1+3i'
b = '1+-2i'
print(complex_number_multiply(a, b))