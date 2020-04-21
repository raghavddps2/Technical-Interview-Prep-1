
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



def bangalore_call(call):
    return call[0][0:5] == '(080)'


def extract_area_code(call):
    call_other_interloc = call[1]

    if call_other_interloc[:2] == '(0':  # Fix land case
        return call_other_interloc.split(sep=')')[0] + ')'

    if call_other_interloc[:3] == '140':  # Telemarketer case
        return call_other_interloc[:3]

    else:  # Mobile case
        return call_other_interloc[:4]


if __name__ == '__main__':
    bng_called_prefix = []
    # Part A
    for call in calls:
        if bangalore_call(call):
            bng_called_prefix.append(extract_area_code(call))

    bng_called_prefix_resum = list(set(bng_called_prefix))
    bng_called_prefix_resum.sort()

    print("\n The numbers called by people in Bangalore have codes:")
    for related_prefix in bng_called_prefix_resum:
        print(related_prefix)

    # Part B
    bng_recurrent_call_num = 0
    for call_prefix in bng_called_prefix:
        if call_prefix == "(080)":
            bng_recurrent_call_num += 1

    print("\n {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
       round(bng_recurrent_call_num/len(bng_called_prefix)*100, 2)))

#Output
# The numbers called by people in Bangalore have codes:
# (022)
# (040)
# (04344)
# (044)
# (04546)
# (0471)
# (080)
# (0821)
# 7406
# 7795
# 7813
# 7829
# 8151
# 8152
# 8301
# 8431
# 8714
# 9008
# 9019
# 9035
# 9036
# 9241
# 9242
# 9341
# 9342
# 9343
# 9400
# 9448
# 9449
# 9526
# 9656
# 9738
# 9740
# 9741
# 9742
# 9844
# 9845
# 9900
# 9961

#  24.81 percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.