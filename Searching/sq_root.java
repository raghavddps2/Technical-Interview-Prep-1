
public class sq_root {

    public static long sqrt(long x){

        long start = 1;
        long end = x/2;
        long ans = -1;
        while(start<=end){
            long mid = (start+end)/2;
            if(mid*mid == x){
                ans = mid;
                return mid;
            }
            if(mid*mid < x){
                start = mid+1;
                ans = mid;
            }
            else{
                end = mid-1; 
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        long val = 12;
        System.out.println(sqrt(val));
    }
    
}