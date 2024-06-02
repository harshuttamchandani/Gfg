#User function Template for python3
class Solution:
    
    def countBuildings(self,arr, n):
        # code here
        count=1
        ele=arr[0]
        for i in range(1,n):
            if ele<arr[i]:
                count=count+1
                ele=arr[i]
        return(count)


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1

# } Driver Code Ends