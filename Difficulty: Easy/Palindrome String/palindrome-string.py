#User function Template for python3


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        flag=1
        while i<j:
            if s[i]!=s[j]:
                flag=0
                break
            else:
                i+=1
                j-=1
        if(flag):
            return True
        else:
            return False
        
		# code here
# recursive way one test case will not pass recursion limit exceeded
# 		if len(s)==1 or len(s)==0:
# 		    return True
# 		if s[0]==s[len(s)-1]:
# 		    return self.isPalindrome(s[1:len(s)-1])
# 		else:
# 		    return False



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Use lowercase 's'
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Print "true" or "false"
        print("~")

# } Driver Code Ends