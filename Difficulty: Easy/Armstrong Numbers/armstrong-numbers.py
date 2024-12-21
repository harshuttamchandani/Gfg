#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        a=n
        ans=0
        while(n!=0):
            rem=n%10
            ans+=rem**3
            n=n//10
        if ans==a:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        flag = ob.armstrongNumber(n)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends