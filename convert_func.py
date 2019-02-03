

def convert(scale:str, temp:float) -> float:
    """ Given temp scale F or C and a float temp, convert temp given to the other scale """

    scale = scale.lower()
    temp = float(temp)

    # If neither, terminate program
    if scale != 'f' and scale != 'c':
        return "Invalid input"

    # If F, convert the temp given to C
    elif scale == 'f':
        # take F temp as input, convert to C, and print
        temp = (temp - 32.0) / 1.8
        return temp

    # If C, convert the temp given to F
    elif scale == 'c':
        # take C temp as input, convert to F, and print
        temp = temp + 32.0 * 1.8
        return temp

print("32\u00b0F is " + str(convert("f", 32)) + "\u00b0C.")
print("75\u00b0F is " + str(convert("f", 75)) + "\u00b0C.")
print("10\u00b0C is " + str(convert("c", 10)) + "\u00b0F.")
print("30\u00b0C is " + str(convert("c", 30)) + "\u00b0F.")