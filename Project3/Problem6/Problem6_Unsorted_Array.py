def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return None
    min = float('inf')
    max = -float('inf')
    for  i in ints:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min,max)
    

## Example Test Case of Ten Integers
import random

print('Normal Cases:')
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


print('Edge Cases:')
l = [i for i in range(300, 301)]  
random.shuffle(l)
print("Pass" if ((300, 300) == get_min_max(l)) else "Fail")


l = []  
print("Pass" if (None == get_min_max(l)) else "Fail")


l = [i for i in range(-24, -1)]  
random.shuffle(l)
print("Pass" if ((-24, -2) == get_min_max(l)) else "Fail")