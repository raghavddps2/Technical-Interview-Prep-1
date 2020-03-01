import java.util.*;
import java.lang.*;
import java.io.*;
class Ques2
 {
	public static void main (String[] args)
	 {
	    try{
           BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
           String s = reader.readLine();
           int T = Integer.parseInt(s.split(" ")[0]);

           for(int i=0;i<T;i++){
               s = reader.readLine();
               int N = Integer.parseInt(s);
                s = reader.readLine();

               int arr[] = new int[N];
                for(int j=0;j<arr.length;j++){
                    arr[j] = Integer.parseInt(s.split(" ")[j]);
                }

                //cyclically rotating by one is simply shifting by one to the right and the last one coming to front.
                int temp = arr[arr.length-1];
                for(int k=arr.length-1;k>0;k--){
                    arr[k] = arr[k-1];
                }

                arr[0] = temp;

                for(int k=0;k<arr.length;k++){
                    System.out.print(arr[k]+" ");
                }
                System.out.println();

           }
	    }
	    catch(Exception e){
	        
	    }
	 }
}