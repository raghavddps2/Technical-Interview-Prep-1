package Arrays.Intermediate;
class stock{
     // Function to find the buy and sell days and print them
     static void stockBuySell(int price[], int n) {
        
        int buy = price[0];
        int sell = 0;
        int bI = 0;
        for(int i=1;i<price.length-1;i++){
            // System.out.println(price[i]+" "+price[i+1]);

            if(price[i] <= buy){
                buy = price[i];
                bI = i;
            }
            if(price[i+1] < price[i]){
                sell = price[i];
                // System.out.println("hi"+i+" "+price.length);
                buy = price[i+1];
                System.out.print("("+bI+" "+i+")"+" ");
                bI = i+1;
            }
            else{
                // System.out.println("hi");
            }
        }
            
        // System.out.println(bI+" "+price[bI]+" "+price[n-1]);
        if(price[bI] != price[n-1] && (bI < (n-1))){
            System.out.print("("+bI+" "+(n-1)+")"+" ");
        }
        if(price[bI] == price[n-1]){
            System.out.print("No Profit");
        }
        }
        
        public static void main(String[] args){

            int arr[] = {23,13,25,29,33,19,34,45,65,67};
            int arr1[] = {4,2,2,2,4};
            stockBuySell(arr1, arr1.length);
            System.out.println(Double.NEGATIVE_INFINITY);
        }
}