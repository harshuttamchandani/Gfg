#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #Your code here
        a={}
        for i in arr:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        n=len(arr)
       # print(a)
        for key, value in a.items():
            if value>n/2:
                return key
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends