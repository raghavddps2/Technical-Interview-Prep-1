package LinkedList;
/**
 * 
 * This is a very important concept of computer science.
 * 
 */
import java.util.HashMap;

class Node{

    int key;
    int value;
    Node prev;
    Node next;

    Node(int key,int value){
        this.key = key;
        this.value = value;
    }
}

class LRUCache{

    private HashMap<Integer,Node> map;
    private int capacity,count;
    private Node head,tail;

    //Constructor, here we have to intitilaize everything.
    public LRUCache(int capacity){
        this.capacity = capacity;
        this.count = 0;
        this.map = new HashMap<>();
        head = new Node(0,0);
        tail = new Node(0,0);

        //Connecting the two nodes.
        head.next = tail;
        tail.prev = head;
        head.prev = null;
        tail.next = null;

    }

    //This is the function to delete the node.
    public void deleteNode(Node node){

        //This is a simple approach to delete the node,
        //as we have padding of head and tail, 
        //No need to worry about a lot of edge cases.
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    //Direct function to add to head of doubly linked list.
    public void addToHead(Node node){

        //Staright forward adding between the head and the tail nodes.
        //This keeps things simple and we don't have to handle a lot of edge cases.
        node.next = head.next;
        head.next.prev = node;
        node.prev = head;
        head.next = node;
    }

    // getMethod
    public int get(int key){

        //If the key exists in the HashMap we retrieve the node address and return the value.
        //When we are just accessing, there is no need for removing it from the list and adding again
        //SO, no 
                // deleteNode(node); and addToNode(node) functions here.
                if(map.get(key) != null){
            Node node = map.get(key);
            int result = node.value;
            return result;
        }
        return -1;
    }
    //setMethod
    public void set(int key,int value){

        //If exists in the map and list, all we have to do is remove from current and get till head.
        if(map.get(key) != null){
            Node node = map.get(key);
            //Setting the value
            node.value = value;
            deleteNode(node);
            addToHead(node);
        }
        //If nothing exists, then we have to add to both hashmap and the doubly linked list.
        else{
            Node node = new Node(key,value);
            map.put(key,node);

            //If count is less than capacity, all we have to do add to the head.
            if(count < capacity){
                addToHead(node);
                count = count + 1;
            }
            //Otherwise, all we have to do is remove the last element, (tail.pre)
            //ANd add this one to the head
            //We have to remove it from the hashmap as well.
            else{
                map.remove(tail.prev.key);
                deleteNode(tail.prev);
                addToHead(node);

            }

        }
    }
}

/*
    Set method.
        - Exist nahi karta
            - Count < capacity:
                - addToHead(node);
                - increment count
            - count > capacity
                - remove(tail.prev);
                - remove from hashMap
                - addToHead;
        - Exist karta hai
            - change the value to the new value
            - deleteNode(node)
            - addToHead(node)
    
    Get Method:
        - HashMap check karo
            - Nahi exist karta:
                - return -1
            - exist karta hai
                - get the NOde corresponsing to the key
                - uska value return kardo
    
    Best Part with constructor:
        - Here, the best part is we have kept padding of head and tail at both the sided of the list
        - So, we have no need to deal with the edge cases.
*/      

//Below code is copied from GeeksForGeeks!!
public class LRU { 
	public static void main(String[] args) 
	{ 
		System.out.println("Going to test the LRU "+ 
						" Cache Implementation"); 
		LRUCache cache = new LRUCache(2); 

		cache.set(1, 10); 

		cache.set(2, 20); 
		System.out.println("Value for the key: 1 is " + 
						cache.get(1)); 
		cache.set(3, 30); 

		System.out.println("Value for the key: 2 is " + 
				cache.get(2));

		cache.set(4, 40); 
		System.out.println("Value for the key: 1 is " + 
			cache.get(1)); 
		System.out.println("Value for the key: 3 is " + 
						cache.get(3)); 
		System.out.println("Value for the key: 4 is " + 
						cache.get(4)); 
	} 
} 