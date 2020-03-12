public class checkPallin {

    public static boolean checkPallinStringFun(String input, int start, int end) {
        if (end <= start) {
            return true;
        }
        if (input.charAt(start) != input.charAt(end)) {
            return false;
        }
        return checkPallinStringFun(input, start + 1, end - 1);
    }

    public static void main(String[] args) {

        String input = "nitin";
        System.out.println(checkPallinStringFun(input, 0, input.length() - 1));
    }
}