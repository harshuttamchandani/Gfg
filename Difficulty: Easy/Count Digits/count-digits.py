#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        k=N
        t=0
        while(N!=0):
            rem=N%10
            if(rem!=0 and k%rem==0 ):
                t+=1
            N=N//10

        return t


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends