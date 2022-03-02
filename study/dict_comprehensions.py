names = ['광일', '광이', '광삼']
comp_dict_names = { 'name' : n  for n in names }
print(comp_dict_names)

# names = ['광일', '광이', '광삼']
# comp_dict_names = { n : 'name' for n in names }
# print(comp_dict_names)


for n in names:
    dict = {}
    dict['name'] = n
    print(dict)

print(dict)
