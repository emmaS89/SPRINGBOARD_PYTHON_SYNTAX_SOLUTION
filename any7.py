def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    for num in nums:
        if num == 7:
            return True

    return False


print(any7([1, 2, 7, 4, 5]))    # True
print(any7([1, 2, 4, 5]))       # False

# ***********************
# OR
# ***********************

def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    return any(num == 7 for num in nums)


print(any7([1, 2, 7, 4, 5]))    # True
print(any7([1, 2, 4, 5]))       # False
