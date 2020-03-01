import java.util.*;
public class Ques9{

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        System.out.println("\nEnter the value of n");

        int n = sc.nextInt();
        int arr[] = new int[n];

        System.out.println("\nENter the array");
        for(int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        // Approach1: We can simply extract the min and the max and then subtarct then (O(n))
        //Approach2 : We can simply sort the array and subtract the fist and the last index. O(nlog(N))

        //For now lets implement approach 2
        Arrays.sort(arr);
        System.out.println("The range of the arrray is "+(arr[arr.length-1]-arr[0]));

    }
}