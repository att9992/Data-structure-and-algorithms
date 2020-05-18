def sort_012(input_list):
    pos_0 = 0
    pos_2 = len(input_list)-1
    front_index = 0
    while front_index <= pos_2:
        if input_list[front_index] == 0:
            input_list[front_index]=input_list[pos_0]
            input_list[pos_0] = 0
            pos_0 +=1
            front_index +=1
        elif input_list[front_index]==2:
            input_list[front_index]=input_list[pos_2]
            input_list[pos_2] = 2
            pos_2 -=1
        else:
            front_index +=1
          
def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == test_case.sort():
        print("Pass")
    else:
        print("Fail")


print('Normal Cases:')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

print('Edge Cases:')
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])

