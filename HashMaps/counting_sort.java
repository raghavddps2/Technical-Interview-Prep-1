import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static int[] sortScores(int[] unorderedScores, int highestPossibleScore) {

        //Now, we will talk about counting sort, this is an algorithm,
        //that we will use to sort the elements in O(n) time and O(n) space.
        
        /**
         * 
         * 1. What we will do is, we will get the maximum.
         * 2. We will create an array of that size.
         * 3. After we create an array of the size, we will go through the 
         *    array and count the occurence of each element.
         * 4. Once we are done doing this, we will start from the end and add to the 
         *      new array, the required number of times.
         * /
        **/
        int countArr[] = new int[highestPossibleScore+1];
        
        for(int i=0;i<unorderedScores.length;i++){
            countArr[unorderedScores[i]]++;
        }
        int track = 0;
        int orderedArr[] = new int[unorderedScores.length];
        for(int i=highestPossibleScore;i>=0;i--){
            for(int occ=0;occ<countArr[i];occ++){
                orderedArr[track] = i;
                track++;
            }
        }
        return orderedArr;
    }


















    // tests

    @Test
    public void noScoresTest() {
        final int[] scores = {};
        final int[] expected = {};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void oneScoreTest() {
        final int[] scores = {55};
        final int[] expected = {55};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void twoScoresTest() {
        final int[] scores = {30, 60};
        final int[] expected = {60, 30};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void manyScoresTest() {
        final int[] scores = {37, 89, 41, 65, 91, 53};
        final int[] expected = {91, 89, 65, 53, 41, 37};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void repeatedScoresTest() {
        final int[] scores = {20, 10, 30, 30, 10, 20};
        final int[] expected = {30, 30, 20, 20, 10, 10};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}