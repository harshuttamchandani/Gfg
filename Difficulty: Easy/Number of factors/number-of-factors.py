#User function Template for python3
class Solution:
    def countFactors (self, N):
        # code here
        c=0
        for i in range(1,int(N**0.5)+1):
            if N%i==0:
                if(N//i!=i):
                    c+=2
                else:
                    c+=1
        
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.countFactors(N))
        print("~")
# } Driver Code Ends