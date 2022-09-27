def find_duplicate(nums):
    nums.sort()
    compar = 0

    for i, num in enumerate(nums):
        if (type(num) == str):
            return False
        if num < 0:
            return False

        if num == compar:
            return num
        else:
            compar = num

    return False
