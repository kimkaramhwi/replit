# Input으로 주어진 list의 각 요소(element)가 해당 list에 몇번 나타나는지 수를 dictionary로 만들어서 return해주세요. Dictionary의 key는 list의 요소 값이며 value는 해당 요소의 총 빈도수 입니다.
# 예를 들어, 다음과 같은 list가 input으로 주어졌다면:
# my_list = ["one", 2, 3, 2, "one"]
# 다음과 같은 dictionary가 return 되어야 합니다.
# {
#    "one" : 2,
#     2 : 2,
#     3: 1
# }

def get_occurrence_count(my_list):
    my_dict = {}

    for value in my_list:
        if value not in my_dict:
            my_dict[value] = 1
        else:
            my_dict[value] += 1
    return my_dict

input = ["one",2,3,2,"one"]
print(get_occurrence_count(input))