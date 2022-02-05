# Input으로 주어진 리스트에서 홀수는 전부 지우고 짝수만 남은 리스트를 리턴해주세요.

def remove_odd_numbers(numbers):
    for i in numbers[:]:
        if i % 2 != 0:
            numbers.remove(i)
    return numbers

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_odd_numbers(input))