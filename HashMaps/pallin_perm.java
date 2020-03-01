/**
 * pallin_perm
 */
import java.util.*;
public class pallin_perm {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String theString = sc.nextLine();
        HashMap<Character,Integer> hm = new HashMap();
        
        for(int i=0;i<theString.length();i++){
            
            if(hm.containsKey(theString.charAt(i))){
                hm.put(theString.charAt(i),hm.get(theString.charAt(i))+1);
            }
            else{
                hm.put(theString.charAt(i),1);
            }
                
        }
        int count = 0;
        for(Character i: hm.keySet()){
            if(hm.get(i)%2 != 0){
                count++;
            }
        }
        if (theString.length()%2 == 0){
            if(count == 0){
                System.out.println("true");
                // return true;
            }
            else{
                System.out.println("false");
                // return false;
            }
        }
        else{
            if(count == 1){
                System.out.println("true");
                // return true;
            }
            else{
                System.out.println("false");
                // return false;
            }
        }


    }
}