def sqrt(number):
    if number == 0 or number == 1:
        return number
    
    start = 0
    end = number //2
    while start < end:
        mid = (start+end)//2
        if mid*mid == number:
            return mid
        elif mid*mid < number:
            start += 1
            result = mid
        else:
            end -=1

    return result

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")