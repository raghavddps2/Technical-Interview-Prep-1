import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    #We define a lookup table to tackle tjis dynamic programming problem.
    lookup_table = [0]*(knapsack_max_weight+1)
#     [print(i,end=" ") for i in range(0,knapsack_max_weight+1)]
#     print()
    for item in items:
        #We will get elements one by one and so on..
        for capacity in reversed(range(knapsack_max_weight+1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity],lookup_table[capacity-item.weight]+item.value)
#             print(lookup_table)
    return lookup_table[-1]

tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    print(test['correct_output'] == max_value(**test['input']))