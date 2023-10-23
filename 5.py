numbers_str = '12,34,56'
numbers_list = numbers_str.split(',')
numbers_sum = sum(map(int, numbers_list))
print(numbers_sum)
