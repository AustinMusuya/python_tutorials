"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 
Constraints:
• -231 <= x <= 231 - 1
 Follow up: Could you solve it without converting the integer to a string?



"""


# Arithmetic Route, uses less memory but still registers time complexity of O log(n)
# Space complexity constant time ; O(1)

def is_palindrome(num):
    # check if num is positive, if it isn't return False
    if num < 0:
        return False
    # intialise variable reverse to 0
    reverse = 0

    # store num in a custom variable so not to change its value
    original = num
    # while loop to create the reverse of original

    while original > 0:
        # get the last digit
        lastDigit = original % 10
        # add this to reverse
        reverse = reverse * 10 + lastDigit
        # create condition to update original for the next iteration
        original = original // 10

    # return num is equal to its reverse
    return reverse == num

# Convert to string method uses more space as compared to the arithmetic route Olog(n)
# Time complexity is the same.


def palindrome_check(num):
    if num < 0:
        return False

    original = str(num)  # Typecast to string

    original = original[::-1]  # reverse the string

    reverse = int(original)  # Typecast back to int

    return reverse == num
