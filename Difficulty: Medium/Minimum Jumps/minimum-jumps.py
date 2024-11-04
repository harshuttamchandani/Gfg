#User function Template for python3
class Solution:
	def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0  # No jumps needed if array size is 0 or 1
        if arr[0] == 0:
            return -1  # Can't move anywhere from the first element
        
        jumps = 0  # Number of jumps made
        current_end = 0  # The farthest point we can reach with the current number of jumps
        farthest = 0  # The farthest point we can reach with the next jump
        
        for i in range(n - 1):
            # Update the farthest we can reach from current index
            farthest = max(farthest, i + arr[i])
            
            # If we have reached the end of the array, return the jumps
            if farthest >= n - 1:
                jumps += 1
                return jumps
            
            # If we reach the end of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest  # We make a jump, update the current end
            
            # If we cannot move forward, return -1
            if current_end <= i:
                return -1
        
        return jumps
	           


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends