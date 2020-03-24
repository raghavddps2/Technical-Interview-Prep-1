package GreedyAlgorithms;
import java.util.*;
public class comp{

    //Creating the class so that we can use our coparator on two of its objects.
    static class Item{

        //We have to declare as non primitive types!!
        Integer roll;
        Integer mark;
        
        //This is our simple constructor that initializes the values.
        public Item(Integer roll,Integer mark){
            this.roll = new Integer(roll);
            this.mark = new Integer(mark);
        }
    }

    public static void main(String[] args){

        //This is the item array we have.
        Item arr[] = new Item[10];

        //Below function initilaizes the array values.
        for(int i=0;i<arr.length;i++){
            double randomDouble = Math.random();
	        randomDouble = randomDouble * 100 + 1;
            int randomInt = (int) randomDouble;
            arr[i] = new Item(i+1,randomInt);
        }

        //This is how we sort the values using the comparator.
        Arrays.sort(arr,new Comparator<Item>(){
            @Override
            public int compare(Item i1,Item i2){

                //We write i2.mark before, this simply implies i am trying to do it in reverse order.
                return i2.mark.compareTo(i1.mark);

                // return i1.mark.compareTo(i2,mark);
                //This is the ascending version of the same.
            }
        });

        //This just prints out the values!
        for(Item i: arr){
            System.out.println(i.roll+" "+i.mark);
        }
        int a = 3;
        System.out.println(a/2);
    }

}