# Input 으로 주어진 리스트에서 오직 한번만 나타나는 값 (unique value)을 
# 가지고 있는 요소는 출력해주세요.

my_list = [1,2,3,4,5,1,2,3,7,9,9,7]

for i in my_list:
    if my_list.count(i) == 1:
        print(i, end="\n")
        