'''
The diamond kata takes as its input a letter, and outputs it in a diamond shape. Given a letter, it prints a diamond starting with 'A', with the supplied letter at the widest point.

Requirements
The first row contains one 'A'.
The last row contains one 'A'.
All rows, except the first and last, have exactly two identical letters.
All rows have as many trailing spaces as leading spaces. (This might be 0).
The diamond is horizontally symmetric.
The diamond is vertically symmetric.
The diamond has a square shape (width equals height).
The letters form a diamond shape.
The top half has the letters in ascending order.
The bottom half has the letters in descending order.
The four corners (containing the spaces) are triangles.
'''
def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let_pos = alphabet.find(letter.upper())
    ## Ensure the input is uppercase
    if let_pos == -1:
        raise ValueError("Input letter must be in the range A-Z")
    used_alpha = alphabet[:let_pos + 1]
    #new group of letters that we will use futher
    row = len(used_alpha)
    result_alpha = []#creating first half of the diamont

    for i, char in enumerate(used_alpha):
        if i == 0:
            result_alpha.append(' ' * (row - (i + 1)) + char + ' ' * (row - (i + 1)))
            #setting the first letter in the middle
        else:
            result_alpha.append(' ' * (row - (i + 1)) + (char) + (' ' * i) +
                                (' ' * (i - 1)) + char + ' ' * (row - (i + 1)))


    result_alpha_reverse = result_alpha[-2::-1]
    # Reverse and exclude the last element
    result = result_alpha + result_alpha_reverse
    return result

