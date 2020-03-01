import java.util.*;
public class Ques1{

    public static void main(String[] args){

        //declaring the scanner
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[10];
        System.out.println("\nEnter the 10 numbers of the array");

        //INPUT
        for(int i=0;i<arr.length;i++){  
            arr[i] = sc.nextInt();
        }

        //OUTPUT
        System.out.println("\nThe 10 elements are");
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        sc.close();
    }
}