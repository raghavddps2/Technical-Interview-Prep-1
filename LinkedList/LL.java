package LinkedList;

/**
 * LL
 */
class Node{
    int data;
    //Self referential structures.
    Node next;

    //Contructor for the node.
    Node(int d){
        this.data = d;
    }
}

class NodeD{
    int data;
    NodeD prev;
    NodeD next;

    NodeD(int d){
        this.data = d;
        this.prev = null;
        this.next = null;
    }

    /*
        1. We can traverse in both directions.
        2. Think when we implement an editor, the forward backward functionality with the doubly linked lists.
        3. The only issue is that we have the node as heavy which can be solved easily using XOR linked List.
        4. Thee dequeue implemnetation is also easy using the doubly linked list!
    */
    /*
        CIRCULAR LINKED LIST
            1. We can traverse the entire list from any node.
            2. We can insert an item both at the beginning and the end using O(n)
            3. This is very good while implementing certain algorithms like round robin etc.

    */
}



class LList{
    //This is initially Null;
    Node head;

    //Method to insert a the beginning of the list.
    void insertBegin(int x){
        Node new_node = new Node(x);
        new_node.next = head;
        head = new_node;
    }

    //This is to insert at the end of the linked list.
    void insertEnd(int x){
        if(head == null){
            insertBegin(x);
            return;
        }
        Node temp = head;
        while(temp.next != null){
            temp = temp.next;
        }
        Node new_node = new Node(x);
        temp.next = new_node;
        return;

    }

    //Method to display the linked list.
    void display(){
        Node temp = head;
        while(temp != null){
            System.out.println(temp.data);
            temp = temp.next;
        }
    }
}
public class LL {
    public static void main(String[] args) {

        //Creating an object of the linkedList class.
        LList ll = new LList();

        //Inserting values into the linkedList at beigin/end.
        ll.insertBegin(10);
        ll.insertBegin(20);
        ll.insertBegin(30);
        ll.insertEnd(40);
        //Displaying the linked list.
        ll.display();
    }
}