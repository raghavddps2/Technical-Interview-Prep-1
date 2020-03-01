import java.util.*;
public class Ques6{

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];

        for(int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();

        //Best is to sort the array, and then tell the kth largest and the kth smallest.
        Arrays.sort(arr);

        System.out.println("\nThe kth smallest is "+arr[k-1]);
        System.out.println("\nThe kth largest is "+arr[arr.length-k]);

    }
}