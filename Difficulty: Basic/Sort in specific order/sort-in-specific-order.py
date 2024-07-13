#User function Template for python3

class Solution:
    def sortIt(self, arr, n):
        odd = []
        even = []
        
        # Separate odd and even numbers
        for i in range(n):
            if arr[i] % 2 == 0:
                even.append(arr[i])
            else:
                odd.append(arr[i])
        
        # Sort odd numbers in descending order
        odd.sort(reverse=True)
        # Sort even numbers in ascending order
        even.sort()
        
        # Combine the sorted lists
        sorted_arr = odd + even
        x=0
        for j in sorted_arr:
            arr[x]=j
            x=x+1
            
            
        
        return arr
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends