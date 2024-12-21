#User function Template for python3


class Solution:
    def sumOfDivisors(self, n):
    	#code here 
    # okayish complexity -: tle after 10 cases
    # 	ans=0
    # 	for i in range(1,n+1):
    # 	    for j in range(1,int(i**0.5)+1):
    # 	        if i%j==0:
    # 	            #print(j,i//j)
    # 	            ans+=j
    # 	            if i//j!=j:
    # 	                #print("here")
    # 	                ans+=i//j
    	                
    # 	    #print(ans)
    
        #optimal
        ans=0
        for i in range(1,n+1):
            ans+=i*(n//i)
    	return ans
    	        
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends