def binary_search_recursive(input_list,number,start_index,end_index):
    if start_index > end_index:
        return -1
    mid_index = (start_index+end_index)//2

    if input_list[mid_index] == number:
        return mid_index
    left_index = binary_search_recursive(input_list,number,start_index,mid_index-1)
    right_index = binary_search_recursive(input_list,number,mid_index+1,end_index)
    return max(left_index,right_index)


def rotated_array_search(input_list, number):
    return binary_search_recursive(input_list,number,0,len(input_list)-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])