def power_2(input):

    if input == 0:
        return 1
    else:
        output = power_2(input-1)
        return 2*output

print(power_2(4))