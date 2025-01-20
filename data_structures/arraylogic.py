numbers = [5,4,6,7,8,9,8,5,4]

new_numbers = []

right = len(numbers) - 1

left = 0

while right > left:
    if numbers[right] not in new_numbers:
        new_numbers.append(numbers[right])
    if numbers[left] not in new_numbers:      
        new_numbers.append(numbers[left])
    right -= 1
    left += 1

print(new_numbers)
