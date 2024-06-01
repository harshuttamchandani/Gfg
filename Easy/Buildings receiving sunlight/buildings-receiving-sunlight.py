#User function Template for python3

class Solution:
    def longest(self, arr, n):
        #Code Here
        count=1
        ele=arr[0]
        for i in range(1,len(arr)):
            if ele<=arr[i]:
                count=count+1
                ele=arr[i]
        return(count)
                
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.longest(arr, n))

        T -= 1


if __name__ == "__main__":
    main()





# } Driver Code Ends