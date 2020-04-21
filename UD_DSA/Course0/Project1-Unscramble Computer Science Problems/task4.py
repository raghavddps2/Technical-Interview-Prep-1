
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def real_numbers_set(texts, calls):
    real_numbers = set()
    for info in texts: # add any texted number
        real_numbers.add(info[0])
        real_numbers.add(info[1])
    for info in calls:
        real_numbers.add(info[1]) # add called number
    return real_numbers

def telemarketers_set(real_numbers, calls):
    scammers = set()
    for info in calls:
        number = info[0]
        if number not in real_numbers:
            scammers.add(number)
    return scammers

def print_answer():
    real_numbers = real_numbers_set(texts, calls)
    scammers = telemarketers_set(real_numbers, calls)
    print("These numbers could be telemarketers: ")
    for number in sorted(scammers):
        print(number)
    pass


print_answer()

#Output
# These numbers could be telemarketers: 
# (022)37572285
# (022)65548497
# (022)68535788
# (022)69042431
# (040)30429041
# (044)22020822
# (0471)2171438
# (0471)6579079
# (080)20383942
# (080)25820765
# (080)31606520
# (080)40362016
# (080)60463379
# (080)60998034
# (080)62963633
# (080)64015211
# (080)69887826
# (0821)3257740
# 1400481538
# 1401747654
# 1402316533
# 1403072432
# 1403579926
# 1404073047
# 1404368883
# 1404787681
# 1407539117
# 1408371942
# 1408409918
# 1408672243
# 1409421631
# 1409668775
# 1409994233
# 74064 66270
# 78291 94593
# 87144 55014
# 90351 90193
# 92414 69419
# 94495 03761
# 97404 30456
# 97407 84573
# 97442 45192
# 99617 25274