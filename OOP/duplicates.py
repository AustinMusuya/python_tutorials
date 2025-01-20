def remove_duplicates(nums):
    # return 0 if array is empty
    if not nums:
        return 0

    # Two pointer approach to remove duplicates in-place

    i = 0
    j = i + 1

    while j < len(nums):
        if nums[j] != nums[i]:  # If the current number is not a duplicate
            i += 1
            nums[i] = nums[j]  # Move it to the next position

        j += 1

    return i + 1  # Length of the array without duplicates


list = [1, 1, 2]
test = remove_duplicates(list)

print(test)
