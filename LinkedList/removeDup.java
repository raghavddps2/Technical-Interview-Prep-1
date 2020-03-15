package LinkedList;

import java.util.HashSet;
import java.util.*;
/**
 * removeDup
 */
public class removeDup {

    public static void main(String[] args) {
        
        HashSet<Integer> hs = new HashSet<Integer>();
        hs.add(1);
        hs.add(2);
        hs.add(3);
        hs.add(4);
        hs.add(5);
        hs.add(1);
        Iterator<Integer> i = hs.iterator(); 
        while (i.hasNext()) 
            System.out.println(i.next());
        Node temp = head;
        Node prev = head;
        while(temp != null){

            prev = temp;
            if(hs.contains(temp.data)){
                temp = temp.next;
            }
            else{
                hs.remove(temp.data);
                prev = temp.next;
                temp = temp.next;
            }
        }
    }
}