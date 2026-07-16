class Solution {
    public int reverse(int x) {
        int num=x;
        int k=0;
        long s=0;

        while (num!=0){
            k=num%10;
            s=s*10+k;
            num/=10;
        }
        if (s > Integer.MAX_VALUE || s < Integer.MIN_VALUE) {
            return 0;
        }
        
        return (int) s; 
    }
}
        


        
    
