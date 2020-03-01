import java.util.*;
public class Ques4{

    public static void main(String[] args){

        int arr[] = new int[10];
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEnter the input(10 elements)");
        
        for(int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }


        //Logic to reverse.
        for(int i=0;i<arr.length/2;i++){

            int temp = arr[i];
                arr[i] = arr[arr.length-i-1];
                arr[arr.length-i-1] = temp;
        }

        //OUTPUT.
        System.out.println("Reverse is :");
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        sc.close();
        System.out.println();
    }
}