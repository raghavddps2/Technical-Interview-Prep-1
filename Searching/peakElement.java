class peakElement{
    
    public static int peakElement1(int arr[],int low,int high,int n){
        
        int mid = (low+high)/2;
        if((mid==0) || (mid == n-1)){
            return mid;
        }
        if(arr[mid] > arr[mid-1] && arr[mid] < arr[mid+1]){
            return mid;
        }
        if(arr[mid] < arr[mid-1]){
            return peakElement1(arr,low,mid-1,n);
        }
        else if(arr[mid] <= arr[mid+1]){
            return peakElement1(arr,mid+1,high,n);
        }
        else{
            return 0;
        }
    }
    public static void main(String[] args) {
        
        int arr[] = new int[]{1,2,3,4,5};
        int low = 0;
        int high = 4;
        int n = 5;
        int ans = peakElement1(arr,low,high,n);
        System.out.println(ans);

    }
}