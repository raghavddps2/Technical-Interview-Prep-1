import java.util.*;

public class Ques2{

        public static void main(String[] args){

            Scanner sc = new Scanner(System.in);
            System.out.println("\n Enter the size of the array");

            int n = sc.nextInt();
            int arr[] = new int[n];
            System.out.println("\n Enter the elements of the array");
            for(int i=0;i<arr.length;i++){
                arr[i] = sc.nextInt();
            }

            System.out.println("\nEnter the number you wanna check");
            int m = sc.nextInt();

            for(int i=0;i<arr.length;i++){

                if(arr[i] == m){
                    System.out.println("TRUE");
                    System.exit(0);
                }
            }
            System.out.println("FALSE");
            sc.close();
        }
}