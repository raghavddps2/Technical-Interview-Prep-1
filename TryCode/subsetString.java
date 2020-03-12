public class subsetString {

    public static void printStrings(String input, String curr, int index) {

        // This is simply the base case, whenever index is same as the length of input,
        // implies we are at the leaf and we need to print.
        if (index == input.length()) {
            System.out.println(curr);
            return;
        }

        // Here, we use the extra char once and once we don't,
        // This is the approach we follow for generating the substrings.
        printStrings(input, curr, index + 1);
        printStrings(input, curr + input.substring(index, index + 1), index + 1);

    }

    public static void main(String[] args) {

        /**
         * input: THe input to the problem is simply the string for which we have to
         * generate the subset strings. curr: This is for the current string to be used.
         * index: This is to keep track.
         */

        String input = "abc";
        String curr = "";
        int index = 0;
        printStrings(input, curr, index);

    }
}