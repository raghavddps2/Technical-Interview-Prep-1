import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def print_first_text(records):
    incoming_number, answering_number, time = records[0]
    print(F"First record of texts, {incoming_number} texts {answering_number} at time {time}")
    pass

def print_last_call(records):
    incoming_number, answering_number, time, duration = records[-1]
    print(F"Last record of calls, {incoming_number} calls {answering_number} at time {time}, lasting {duration} seconds")
    pass


print_first_text(texts)
print_last_call(calls)

#output
# First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22
# Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15, lasting 2151 seconds