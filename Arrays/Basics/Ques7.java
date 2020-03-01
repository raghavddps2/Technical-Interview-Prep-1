import java.util.*;
public class Ques7{

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int arr[] = new int[n];
        for(int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        System.out.println("Enter the number you wanna search");
        int m = sc.nextInt();
        int count = 0;
        for(int i=0;i<arr.length;i++){
            if(arr[i] == m){
                count++;
            }
        }
        System.out.println("The occurence of "+m+" is "+count+" times");
        sc.close();
    }
}