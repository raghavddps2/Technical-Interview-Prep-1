# `Explanation to the Square root problem`


1. We are supposed to find the square root of a given number, following was the first naive approach I came up with.

    * To get to the integer square root of a number, we can iterate till (number/2) and stop just at the point where the number squares is greater than the number for which we want to get the square root.

2. But as the problem demanded an O(log(n)) solution, I though if I could apply binary search to the problem, and yeah, tthat worked out.
    * Maintain a start and an end pointer , and we run the loop till there is slight difference between the low and the high pointer and after some iterations we end up with the square root.

3. Another interesting method, I learnt during my coursework at college, was newton raphson, method and that also did the task very well.

4. Time complexity: O(log(n))
5. Space Complexity: O(1)
