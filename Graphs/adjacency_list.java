import java.util.*;
class Graph{

    //We define the values.
    ArrayList<ArrayList<Integer>> adj;
    int n;
    //We define the constructor where we initialize everything we need for the graph.

    
    public Graph(int n){

        //We have to initialize it here.
        this.adj = new ArrayList<ArrayList<Integer>>(n);
        //All we have to do is initialize the ineer dynamic array lists.
        for(int i=0;i<n;i++){
            adj.add(new ArrayList<Integer>());
        }
        this.n = n;
    }

    //This is simply adding an edge to the graph.
    public void addEdge(int u,int v){
        adj.get(u).add(v);
        adj.get(v).add(u);
    }

    //This is just for printing the graph!
    public void printGraph(){
        for(int i=0;i<adj.size();i++){
            System.out.println("\nAdjacency list for vertex "+i);
            for(int j=0;j<adj.get(i).size();j++){
                System.out.print("->"+adj.get(i).get(j));
            }
        }
    }

}

public class adjacency_list{
    public static void main(String[] args) {
        
        int n = 4;

        //This is getting an object of the graph class.
        Graph g = new Graph(n);
        g.addEdge(0,1);
        g.addEdge(0,2);
        g.addEdge(2,3);
        g.addEdge(1,2);
        g.printGraph();
    }
}