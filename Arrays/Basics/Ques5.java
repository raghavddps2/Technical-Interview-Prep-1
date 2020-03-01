import java.util.Scanner;

public class Ques5{

    public static void main(String[] args){

        //Using the most basic sort, that is the bubble sort here.
        /* In the bubble sort,

            the basic concept is that, we just bubble the largest element at the last at each iteration.
        */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int arr[] = new int[n];
        //INPUT.
        for(int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        //Sorting logic
        for(int i=0;i<arr.length-1;i++){

            //check for the largest one inside and send it to the last step by step.
            for(int j=0;j<arr.length-i-1;j++){
                
                if(arr[j]>arr[j+1]){
                    int myVar = arr[j];
                        arr[j] = arr[j+1];
                        arr[j+1] = myVar;
                }   
            }
        }

        //NOw, the array is sorted.
        System.out.println("\nThe answer is: ");
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
}