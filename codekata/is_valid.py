def is_valid(string):
	left = ['(', '{', '[']
	right = [')', '}', ']']
	stack = []
	
	for i in string:
		if i in left:
			stack.append(i)
		elif i in right:
			if len(stack) <= 0:
				return False
			if left.index(stack.pop()) != right.index(i):
				return False
	return len(stack) == 0
            
print(is_valid("(({}"))
print(is_valid('([{}])'))
print(is_valid('()[]{}'))