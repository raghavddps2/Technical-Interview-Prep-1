import java.util.*;
import java.lang.*;
import java.io.*;

/**
 * 
 * Tried the usual array way, using the array and then checking in other, basically takes O(M*N) time.
 * With hashmap we do it in O(M or N) whichever is greater time.
 * Getting TLE with java.
 */

class Ques1
 {
    public static void main (String[] args)
    {
        String str1 = "";
        String str2 = "";
        String str3 = "";
        BufferedReader reader = new BufferedReader(new InputStreamReader(
            System.in));
        try{
            str1 = reader.readLine();
        }
        catch(Exception e){
            
        }

        int T = Integer.parseInt(str1.split(" ")[0]);
        for(int k=0;k<T;k++){
            Map<Integer,Integer> map = new HashMap<Integer,Integer>();
            try{
                str1 = reader.readLine();
                str2 = reader.readLine();
                str3 = reader.readLine();
            }
            catch(Exception e){
            
            }
            int N = Integer.parseInt(str1.split(" ")[0]);
            int M = Integer.parseInt(str1.split(" ")[1]);
            
            int arr1[] = new int[N];
            int arr2[] = new int[M];
            
            for(int j=0;j<N;j++){
                arr1[j] = Integer.parseInt(str2.split(" ")[j]);
            }
            for(int j=0;j<M;j++){
                arr2[j] = Integer.parseInt(str3.split(" ")[j]);
            }
            for(int i=0;i<N;i++){
                map.put(arr1[i],1);
            }
            for(int i=0;i<M;i++){
                map.put(arr2[i],1);
            }
        
            System.out.println(map.size());
        }
        try{
            reader.close();
        }
        catch(Exception e){

        }
    }	
}