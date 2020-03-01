import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
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
                int sum2 = N*(N+1)/2;
               int arr[] = new int[N];
                for(int j=0;j<arr.length-1;j++){
                    arr[j] = Integer.parseInt(s.split(" ")[j]);
                    sum2 -= arr[j];
                }
                System.out.println(sum2);
                
                
           }
    	 }
    	 catch(Exception e){
    	     
    	 }
        
	 }
}