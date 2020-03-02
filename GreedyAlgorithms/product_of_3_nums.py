
import unittest


def highest_product_of_3(list_of_ints):

    if len(list_of_ints) < 3:
        raise ValueError("Not enough values!!")
    
    #Now, this is reallly interesting, all we have to do is get the highest product
    #of 3 in a list_of_ints
    
    """
        Approach 1:
            One straight forward direct approach is to run a loop but that
            complexity will come around O(n^3)
        Approach 2:
            Another direct approach is to use sorting and directly use the last 3,
            but this approach simply fails when we have negative elements!!
        
        Approach 3:
            Now, here comes the interesting part, our greedy solution!
            What greedy solution says is, 
                We keep track of the
                    highest
                    lowest
                    product of highest 3
                    product of two highest
                    product of two lowest
    """
    
    minimum = min(list_of_ints[0],list_of_ints[1])
    maximum = max(list_of_ints[0],list_of_ints[1])
    
    product_of_2_highest = list_of_ints[0]*list_of_ints[1]
    product_of_2_lowest = list_of_ints[0]*list_of_ints[1]
    product_of_3_highest = list_of_ints[0]*list_of_ints[1]*list_of_ints[2]
    
    for i in range(2,len(list_of_ints)):
        current = list_of_ints[i]
        
        product_of_3_highest = max(product_of_3_highest,current*product_of_2_highest,current*product_of_2_lowest)
        product_of_2_highest = max(product_of_2_highest,current*maximum,current*minimum)
        product_of_2_lowest = min(product_of_2_lowest,current*minimum,current*maximum)
        minimum = min(minimum,current)
        maximum = max(maximum,current)
        
    

    return product_of_3_highest
# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)