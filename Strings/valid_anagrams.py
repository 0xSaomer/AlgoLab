# This function checks if two given strings are anagrams of each other.
# An anagram contains the same characters in a different order, such as "listen" and "silent"
# Returns True if they are anagrams, otherwise False.

def anagrams(str1, str2):
    # Check if the lengths of the strings are unequal — if so, they can't be anagrams.
    if len(str1) != len(str2):
        return False
    # Return True if the sorted strings match (i.e., same characters in any order).
    return sorted(str1) == sorted(str2)


print(anagrams(str1='abc', str2='cab'))
print(anagrams(str1='abc', str2='cabs'))