// https://practice.geeksforgeeks.org/problems/quick-sort/1 
//The above is the practice link for the same.
//In the problem only function was asked to implement.

static int partition(int arr[], int low, int high)
    {
        int pivot = arr[high];
        int i = low-1; 
        //Here, i is basicallly a variable that we use to iterate on the array from scratch.
        
        for(int j=low;j<high;j++){
            //If comes out to be greater we replace the ith element and the arr[j]
            if(arr[j] <= pivot){
                
                i++;
                
                int var = arr[j];
                    arr[j] = arr[i];
                    arr[i] = var;
            }
        }
        
        //Finally we will put the pivot of the correct position.
        int var = pivot;
            arr[high] = arr[i+1];
            arr[i+1] = var;
            
            //So, finally the partition will be at the point i+1
            //Before this everything will be smaller after this everything will be larger
            
        return (i+1);
    }