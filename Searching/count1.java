/**
 * count1
 */
public class count1 {

    public static int lIndex(int arr[],int low,int high){

        int mid = (low+high)/2;
        if(low>high){
            return -1;
        }
        if(arr[mid] == 1 &&(mid == 0 || (arr[mid-1] != 1))){
            return mid;
        }
        if(arr[mid] == 1 && (arr[mid] == arr[mid-1])){
            return lIndex(arr,low,mid-1);
        }
        else{
            return lIndex(arr,mid+1,high);
        }


    }

    public static int rIndex(int arr[],int low,int high){
        //Approach:
            // 1. First step is to calculate the mid.
            // 2. If mid == 1 and (mid == n-1 or mid+1 != mid). return mid;
            // 3. All we have to do is recursive approach if the right is same as left to forward.
            // 4. Else, allwe do is to usual go backward.
            int mid = (low+high)/2;

            if(low>high){
                return -1;
            }
            if(arr[mid] == 1 && ((mid == arr.length-1) || (arr[mid] != arr[mid+1]))){
                return mid;
            }

            if(arr[mid] == 1 && (arr[mid] == arr[mid+1])){
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
        int arr[] = new int[]{0,1,1,1,1,1,1,1,1,1,1,1,1,1};
        int lIndex = lIndex(arr,0,arr.length-1);
        System.out.println(lIndex);
        int rIndex = rIndex(arr,0,arr.length-1);
        System.out.println(rIndex);
        if(lIndex == -1 && rIndex == -1){
            System.out.println(0);
            return;
        }
        int number =  rIndex-lIndex+1;
        System.out.println(number);
    }
}