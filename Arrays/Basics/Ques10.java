import java.util.*;
public class Ques10{

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int arr[] = new int[n];
        System.out.println("\nEnter the array");
        
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }

        //NOw, we will just shift the elements to front if they are negative, simple enough approach.
        //This works in O(n)
        int arrayRef = 0;
        for(int i=0;i<arr.length;i++){
            if(arr[i] < 0){
                int temp = arr[i];
                    arr[i] = arr[arrayRef];
                    arr[arrayRef] = temp;
                arrayRef++;
            }
        }

        System.out.println("The new array with negative elements to the left is: ");
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
}