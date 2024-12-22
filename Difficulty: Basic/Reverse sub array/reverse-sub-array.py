#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		if l>r:
		    return arr
		temp=arr[l-1]
		arr[l-1]=arr[r-1]
		arr[r-1]=temp
		return self.reverseSubArray(arr,l+1,r-1)


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        l = int(input())
        r = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.reverseSubArray(arr, l, r)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends