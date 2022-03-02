a1 = [6, 3, 9]
print('a1:', a1)
a2 = a1.sort() # 원본을 정렬하고 수정합니다(in-place)
print('-----정렬 후-----')
print('a1:', a1)
print('a2:', a2)

b1 = [6, 3, 9]
print('b1:', b1)
b2 = sorted(b1) # 원본은 유지하고 정렬한 새 리스트를 만듭니다
print('-----정렬 후-----')
print('b1:', b1)
print('b2:', b2)