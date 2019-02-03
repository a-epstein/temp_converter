# Convert F temperature to C temperature
# F = C * 1.8 + 32
# C = F - 32 / 1.8

deg = '\u00b0'

# Ask user if the temp they want to convert is in F or C
scale = input("Is your temperature in F or C?: Enter F for Fahrenheit or C for Celsius: ").lower()

# If neither, terminate program
if scale != 'f' and scale != 'c':
    print("Neither F nor C input")

# If F, convert the temp given to C
elif scale == 'f':
    print("Temp in F")

    # take F temp as input, convert to C, and print
    f = float(input("Enter temperature in F: "))
    c = (f - 32.0) / 1.8
    print(str(f) + deg + "F is " + str(c) + deg + "C.")

# If C, convert the temp given to F
elif scale == 'c':
    print("Temp in C")

    # take C temp as input, convert to F, and print
    c = float(input("Enter temperature in C: "))
    f = (c + 32.0) * 1.8
    print(str(c) + deg + "C is " + str(f) + deg + "F.")