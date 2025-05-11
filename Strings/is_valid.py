# This function calculates valid brackets

def is_valid(str):

    # a stack to keep track of brackets
    stack = []
    # hash_map to reference the brackets
    hash_map = {')': '(', '}': '{', ']': '['}

    for i in str:
        # if an opening bracket is found in hash_map, it is stored in the stack
        if i in hash_map.values():
            stack.append(i)

        # if a closing bracket is found, we check if it matches top of the stack
        # if it does, we found a match, else we return False
        if i in hash_map.keys():
            if stack and stack[-1] == hash_map[i]:
                stack.pop()

            else:
                return False

    return not stack


# Example 1
str = "()"
print(is_valid(str))  # Output: True

# Example 2
str = "()[]{}"
print(is_valid(str))  # Output: True

# Example 3
str = "(]"
print(is_valid(str))  # Output: False

# Example 4
str = "([)]"
print(is_valid(str))  # Output: False

# Example 5
str = "{[]}"
print(is_valid(str))  # Output: True
