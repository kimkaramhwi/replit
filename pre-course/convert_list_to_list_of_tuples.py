def convert_list_to_list_of_tuples(my_list):
    my_tuple = []
    my_tuple.append((my_list[0], my_list[1]))
    my_tuple.append((my_list[2], my_list[3]))
    my_tuple.append((my_list[4], my_list[5]))
    return my_tuple

input = [1,2,3,4,5,6]
print(convert_list_to_list_of_tuples(input))