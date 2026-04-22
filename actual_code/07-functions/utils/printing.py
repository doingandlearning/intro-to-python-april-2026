# define a function with def
def print_message_with_borders(message, border_length=10, border="*"):
    """
    A function that prints out a message with borders
    """
    print(border * border_length)
    print(message)
    print(border * border_length)
    return message

print_message_with_borders(message="Meyrin is very nice", border="=")
print_message_with_borders(border_length=15, message="Not as nice as Geneva", border="-")
result = print_message_with_borders("Saint-Genis is best", 20, "-*-")

print(result)
