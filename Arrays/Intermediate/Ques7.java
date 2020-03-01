// This is the code, there is some problem with the java judge, one test case has wrong input in the question.
/**
 * 
 * First approach: Using Maps, solves it in O(n)
 * Another approach using straight array traversal if equal we increment all the indexes
 * If arr1[i] < arr2[j], we increment i, as obviously now that will never come,
 * same case for arr2 and arr3
  
 */
import java.util.*;
import java.lang.*;
import java.io.*;
class Ques7
 {
	public static void main (String[] args)
	 {
	    HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
	    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	    
		try{
			int T = Integer.parseInt(reader.readLine());
			String s = reader.readLine();
		  for(int j=0;j<T;j++){
				int n1 = Integer.parseInt(s.split(" ")[0]);
				int n2 = Integer.parseInt(s.split(" ")[1]);
				int n3 = Integer.parseInt(s.split(" ")[2]);
				
				int arr1[] = new int[n1];
				int arr2[] = new int[n2];
				int arr3[] = new int[n3];
				
				String s1 = reader.readLine();
				String s2 = reader.readLine();
				String s3 = reader.readLine();

				for(int i=0;i<n1;i++){
					arr1[i] = Integer.parseInt(s1.split(" ")[i]);
					if(map.containsKey(arr1[i])){
						map.replace(arr1[i],map.get(arr1[i])+1);
					}
					else{
						map.put(arr1[i],1);
					}
					
				}
				for(int i=0;i<n2;i++){
					arr2[i] = Integer.parseInt(s2.split(" ")[i]);
					if(map.containsKey(arr2[i]) && map.get(arr2[i]) == 1){
						map.replace(arr2[i],map.get(arr2[i])+1);
					}
					else{
						map.put(arr2[i],1);
					}
				}
				for(int i=0;i<n3;i++){
					arr3[i] = Integer.parseInt(s3.split(" ")[i]);
					if(map.containsKey(arr3[i]) && map.get(arr3[i]) == 2){
						map.replace(arr3[i],map.get(arr3[i])+1);
					}
					else{
						map.put(arr3[i],1);
					}
				}
					map.forEach((K,V) -> System.out.println(K+" "+V));
				int flag = 0;
				for(int i : map.keySet()){
					if(map.get(i) == 3){
						System.out.print(i+" ");
						flag = 1;
					}
				}
				if(flag == 0){
				    System.out.println("-1");
				    continue;
				}
				System.out.println();
				
			
		  }
		}
		catch(Exception e){
			//
		}
			
		}
		
	 }
