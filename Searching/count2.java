public class count2 {

    //Not required.
    // public static int lIndex(int arr[],int low,int high){

    //     int mid = (low+high)/2;
    //     if(arr[mid] == 1 && (mid == 0 || (arr[mid] != arr[mid-1]))){
    //         return mid;
    //     }
    //     if(arr[mid] < 1 ){
    //         return lIndex(arr,mid+1,high);
    //     }
    //     else{
    //         return lIndex(arr,low,mid-1);
    //     }
    // }

    public static int rIndex(int arr[],int low,int high){
     
        int mid = (low+high)/2;
        if(arr[mid] == 1 && ((mid == (arr.length-1)) || (arr[mid] != arr[mid+1]))){
            return mid;
        }
        if(arr[mid] == 1 && arr[mid] ==  arr[mid+1] ){
            return rIndex(arr,mid+1,high);
        }
        else{
            return rIndex(arr,low,mid-1);
        }
        
    }
    public static void main(String[] args) {
        
        //Approach
            // The approach to this is pretty straight forward.
        // 1. Calculate the left most index of 1.
        // 2. Calculate the right mmost index of 1.
        // 3. return rightMost-leftMost+1
        int arr[] = new int[]{1,1,1,0,0,0,0,0,0,0};
        int lIndex = -1;
        if(arr[0] != 0){
            lIndex = 0;
        }
        System.out.println(lIndex);
        int rIndex = rIndex(arr,0,arr.length-1);
        System.out.println(rIndex);
        if(lIndex == -1 && rIndex == -1){
            System.out.println(0);
            return;
        }
        int number =  rIndex-lIndex+1;
        System.out.println(number);
        return;
    }
}