def minimum(numbers_list):
    min = numbers_list[0]
    for index in range(len(numbers_list)):
        if numbers_list[index] < min:
            min = numbers_list[index]
    return min

def maximum(numbers_list):
    max = numbers_list[0]
    for index in range(len(numbers_list)):
        if numbers_list[index] > max:
            max = numbers_list[index]
    return max

def sorting(numbers_list):
    sorted_list = []
    copy_list = numbers_list.copy()
    while len(copy_list) != 0:
        sorted_list.append(minimum(copy_list))
        copy_list.remove(minimum(copy_list))
    return sorted_list

numbers_list = [3, 7, 5, 10, 1]
sorted_list = sorting(numbers_list)
print(sorted_list)
min = minimum(numbers_list)
max = maximum(numbers_list)
print(min)
print(max)