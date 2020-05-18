def merge(left,right,bool=False):
    merged=[]
    left_index = 0
    right_index = 0
    if bool:
        left_num = ''
        right_num=''
        to_left = True
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                if to_left == True:
                    left_num=str(right[right_index])+left_num
                else:
                    right_num=str(right[right_index])+right_num
                right_index +=1
            else:
                if to_left == True:
                    left_num=str(left[left_index])+left_num
                else:
                    right_num=str(left[left_index])+right_num
                left_index +=1
            to_left = not to_left

        while left_index < len(left):   
            if to_left:
                left_num = str(left[left_index]) + left_num
            else:
                right_num = str(left[left_index]) + right_num
                
            left_index += 1
            to_left = not to_left

        while right_index < len(right):  
            if to_left:
                left_num = str(right[right_index]) + left_num
            else:
                right_num = str(right[right_index]) + right_num

            right_index += 1
            to_left = not to_left

        return [int(left_num), int(right_num)]

    else:
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(right[right_index])
                right_index +=1
            else:
                merged.append(left[left_index])
                left_index +=1


        merged += left[left_index:]
        merged += right[right_index:]

        return merged


def rearrange_digits(input_list,bool=False):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = rearrange_digits(left)
    right = rearrange_digits(right)

    return merge(left, right, bool)

def test_function(test_case):
    output = rearrange_digits(test_case[0],bool = True)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print('Normal Cases:')
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [852, 964]])

print('Edge Cases:')
test_function([[1, 1, 1], [11, 1]])
test_function([[1], [1]])
test_function([[], []])

