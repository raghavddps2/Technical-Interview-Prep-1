import java.util.Arrays;

public class recSearch {

    public static boolean recSearchFun(int arr[], int key) {

        if (arr.length == 0) {
            return false;
        }
        if (arr[0] == key) {
            return true;
        }
        return recSearchFun(Arrays.copyOfRange(arr, 1, arr.length), key);
    }

    public static void main(String[] args) {

        int arr[] = { 1, 2, 3, 4, 5 };
        int key = 10;
        System.out.println(recSearchFun(arr, key));

    }
}