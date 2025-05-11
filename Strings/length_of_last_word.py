class Solution:
    def length_of_last_word(self, str):
        # Strip leading and trailing whitespaces to clean the string
        s_string = str.strip()

        # Split the string by spaces, creating a list of words
        new_string = s_string.split(' ')

        # Get the last word in the list
        last_word = new_string[-1]

        # Return the length of the last word
        return len(last_word)


sol = Solution()
print(sol.length_of_last_word(str="fly me   to   the moon"))
