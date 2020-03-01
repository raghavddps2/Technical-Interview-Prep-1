import java.util.*;
public class Ques3{

    public static void main(String[] args){

        int arr[] = new int[10];
        Scanner sc = new Scanner(System.in);
        //INPUT
        for(int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        int max = 0;
        int min = Integer.MAX_VALUE;

        for(int i=0;i<arr.length;i++){
            if(arr[i] > max){
                max = arr[i];
            }

            if(arr[i] < min){
                min = arr[i];
            }
        }

        System.out.println("MAX: "+max+" MIN: "+min);
        sc.close();
    }
}