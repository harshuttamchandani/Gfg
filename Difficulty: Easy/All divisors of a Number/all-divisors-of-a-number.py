#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def print_divisors(self, N):
        # code here
        l=set()
        for i in range(1,int(N**0.5+1)):
            if N%i==0:
                l.add(i)
                l.add(N//i)
        a=list(l)
        a.sort()
        for i in a:
            print(i,end=' ')


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
        print("~")
# } Driver Code Ends