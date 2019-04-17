def is_palindrome(input_string):
    """Eval lower case input_string value to same reversed value"""
    if input_string.casefold() == input_string.casefold()[::-1]:
        print("True")
    else:
        print("False")

is_palindrome("tacocat")