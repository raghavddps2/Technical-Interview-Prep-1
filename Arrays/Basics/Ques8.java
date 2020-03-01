import java.util.Scanner;

public class Ques8{

    public static void main(String[] args){

        //Approach: Simply count the occurences of 0 and 1 and get that of 2.
        //Assign the new values to the indexes.
        //This is doing the task in O(n), but i think it can be optimized to o(log(n))

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int arr[] = new int[n];
        for(int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        int count0 = 0;
        int count1 = 0;
        int count2 = 0;
        //NOw counting the same
        for(int i=0;i<arr.length;i++){
            if(arr[i] == 0){
                count0++;
            }

            if(arr[i] == 1){
                count1++;
            }
        }
        count2 = arr.length-count0-count1;

        //NOw, substituting the values.
        int i=0;
        for(int j=0;j<count0;j++){
            arr[i] = 0;
            i++;
        }
        for(int j=0;j<count1;j++){
            arr[i] = 1;
            i++;
        }
        for(int j=0;j<count2;j++){
            arr[i] = 2;
            i++;
        }

        //Now, printing the sorted array.
        System.out.println("\nThe sorted array is ");
        for(int k=0;k<arr.length;k++){
            System.out.print(arr[k]+" ");
        }
        System.out.println();
    }
}