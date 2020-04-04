def recursive(input):

    if input <=0:
        return input
    else:
        output = recursive(input-1)
        print(output)
        return output

print(recursive(2))