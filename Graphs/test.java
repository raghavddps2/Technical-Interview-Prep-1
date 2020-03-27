import java.util.*;
public class test {

    public static void main(String[] args) {
        
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(1);
        arr.add(2);
        arr.remove(0);

        for (Integer integer : arr) {
            System.out.println(integer);
        }
    }
    
}