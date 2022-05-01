def create_acronym(message):
    """creates acronym from message
    (str) -> str
    >>> create_acronym("Hello World")
    'HW - Hello World'
    """
    result = ""
    message = message.split(sep="\n")
    final_result = ""
    for amount in range(len(message)):
        temp = message[amount]
        temp = temp.split(sep=' ')
        for first_letter in range(len(temp)):
            temp2 = temp[first_letter]
            temp2 = temp2[:1]
            result = result + temp2
        result = result + " "
    result = result.upper()
    result = result.split(sep=" ")
    result = result[:-1]
    for lines in range(len(result)):
        result[lines] = result[lines] + " - " + message[lines]
        if lines < len(result)-1:
            final_result = final_result + result[lines] + "\n"
        else:
            final_result = final_result + result[lines]
    return final_result
