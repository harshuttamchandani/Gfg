#User function Template for python3

# arr is the array
# n is the number of element in array
def SumArray(arr,n):
     # your code here
     ans=0
     for i in range(n):
         ans=ans+int(arr[i])
     for j in range(n):
         arr[j]=ans-int(arr[j])
     return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    t = int(input())
    
    while(t >= 1):
        n = int(input())
        arr = input().split();
        SumArray(arr,n)
        print(*arr)
        t -= 1
        
if __name__ == '__main__':
    main()
# } Driver Code Ends