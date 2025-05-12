def reverse_words(sentence):
    # Remove leading and trailing whitespace
    sentence = sentence.strip()

    # Split the sentence into a list of words
    new_str = sentence.split()

    # Initialize two pointers to reverse the list in place
    left, right = 0, len(new_str) - 1
    while left < right:
        # Swap the words at left and right pointers
        new_str[left], new_str[right] = new_str[right], new_str[left]
        left += 1
        right -= 1

    # Join the reversed list of words into a string
    return " ".join(new_str)


print(reverse_words(sentence="Reverse this sentence"))
