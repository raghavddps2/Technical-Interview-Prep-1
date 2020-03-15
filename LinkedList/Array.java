package LinkedList;
import java.util.*;
/**
 * Array
 */
public class Array {

    public static void main(String[] args) {
                
        int arr[] = new int[200];
        int[] arr1 = new int[100];
        ArrayList<Integer> arr2 = new ArrayList<Integer>();        
        System.out.print(arr[0]);
        System.out.print(arr1[0]);
        System.out.print(arr2.get(0));
    
        
        /*
            1. The sspace allocated for arrays is fixed. 
            2. ArrayList solves by doubling every time it is full.
            3. Insertion in the middle is costly.
            4. Deletion from the middle is costly as well.
            5. Implementationof data structures like queue or dequeue is difficult with arrays.
            6. Round Robin Scheduling.
                    This is difficult with array and easy with LinkedList
            7. Implementing sequence of items questions is even difficult for the same.
            8. Even while combining two sorted linked list, Linked Lists are goood to use.

            9. The best part about linked list os that elements do not have to be necessarily at contigious locations.

        */
    }
}