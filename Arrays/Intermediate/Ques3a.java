import java.util.*;
import java.lang.*;
import java.io.*;
class Ques3a
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
                int ans = 0;
               int arr[] = new int[N];
                for(int j=0;j<arr.length-1;j++){
                    arr[j] = Integer.parseInt(s.split(" ")[j]);
                    ans = ans^(j+1);
                    ans = ans^arr[j];
                }
                ans = ans^N;
                //Now, only that which has not come twice will be left, result will be answer we need. 
                System.out.println(ans);
                
                
           }
    	 }
    	 catch(Exception e){
    	     
    	 }
        
	 }
}