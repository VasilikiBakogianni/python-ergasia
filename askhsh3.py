def rot13_converter(x):
    result = ""

# Loop over characters.
    for y in x:
# Convert to number with ord.
        c = ord(y)

# Shift number back or forward.
        if c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        elif c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13

        result += chr(c)

# Print the encrypted text
    return result

text = raw_input("Type your text: ")
print(rot13_converter(text))


