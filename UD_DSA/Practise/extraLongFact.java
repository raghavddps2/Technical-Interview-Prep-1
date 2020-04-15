package Practise;
import java.util.*;
/**
 * extraLongFact
 */
public class extraLongFact {

    public static int multiply(int n,int k) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        int number_ref = n;
        while(number_ref != 0){
            int value = number_ref%10;
            number_ref = (int)(number_ref/10);
            arr.add(value);
        }
        int carry = 0;
        int i=0;
        for(;i<arr.size();i++){
            int temp_ref = arr.get(i)*k+carry;
            int new_arr_val = temp_ref%10;
            arr.set(i,new_arr_val);
            carry = (int)(temp_ref/10);
        }
        if (carry != 0){
            arr.add(i,carry);
        }
        String str = new String();
        for(int j=arr.size()-1;j>-1;j--){
            str = str + Integer.toString(arr.get(j));
        }
        return Integer.parseInt(str);
    }
    public static ArrayList<Integer> multiplyArrayList(ArrayList<Integer> arr,int k) {

        int carry = 0;
        int i=0;
        for(;i<arr.size();i++){
            int temp_ref = arr.get(i)*k+carry;
            int new_arr_val = temp_ref%10;
            arr.set(i,new_arr_val);
            carry = (int)(temp_ref/10);
        }
        if (carry != 0){
            arr.add(i,carry);
        }
        return arr;
    }
    

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        int number_ref = n;
        while(number_ref != 0){
            int value = number_ref%10;
            number_ref = (int)(number_ref/10);
            arr.add(value);
        }   
        while(n != 1){
            arr = multiplyArrayList(arr,n-1);
            n = n-1;
        }
        String str = new String();
        for(int j=arr.size()-1;j>-1;j--){
            str = str + Integer.toString(arr.get(j));
        }
        System.out.println(str);
    }
}