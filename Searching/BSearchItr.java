package Searching;
class BSearchItr{

    public static int bSearchitr(int[] arr,int low,int high,int x){
        int low_itr = low;
        int high_itr = high;
        int mid = (low+high)/2;
        while(low_itr<=high_itr){
            mid = (low_itr+high_itr)/2;
            if(arr[mid] == x){
                return mid;
            }
            
            if(arr[mid] < x){
                low_itr = mid + 1;
            }
            else{
                high_itr = mid-1;
            }
        }
        return -1;
    }

    public static int bSearchrec(int[] arr,int low,int high,int x){

        int mid = (low+high)/2;
        if(low > high){
            return -1;
        }
        if(arr[mid] == x){
            return mid;
        }
        if(arr[mid] < x){
            return bSearchrec(arr,mid+1,high, x);
        }
        else{
            return bSearchrec(arr, low, mid-1, x);
        }
    }

    public static void main(String[] args) {
        
        //Linear Search
        // for(int i=0;i<n;i++){
        //     if(arr[i] == x){
        //         return i;
        //     }
        // }
        // return -1;
        int arr[] = new int[]{1,2,3,4,5,6};
        int low = 0;
        int high = arr.length;
        int x = 3;
        //Binary Search function() - Iterative
        bSearchitr(arr,low,high,x);

        //Binary Search function() - Recursive.
        bSearchrec(arr,low,high,x);
    }
}