def pair_sum_to_zero(input_list, target):
    dict1 = dict()
    for i in range(0,len(input_list)):
        if (target - input_list[i]) in dict1:
            return [i,dict1[target-input_list[i]]]
        dict1[input_list[i]] = i
    return -1

def test_function(test_case):
    output = pair_sum_to_zero(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)