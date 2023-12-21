//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++

class Solution{
public:
    //Function to reverse every sub-array group of size k.
    void reverseInGroups(vector<long long>& arr, int n, int k){
        // code here
        if(k>n)
        {
            reverse(arr.begin(),arr.end());
            return;
        }
        int i=0;
        int j=k-1;
        int c=0;
        
        while(j<n&&c<2)
        {
        
        reverse(arr.begin()+i,arr.begin()+j+1);
    
        i=i+k;
        
        if((j+k)<n)
        {
        j=j+k;
        }
        else
        {
            j=n-1;
            c++;
        }
        
        }



    }
};

//{ Driver Code Starts.
int main() {
    int t; 
    cin >> t; 
    while(t--){ 
        int n;
        cin >> n; 
        vector<long long> arr; 
        int k;
        cin >> k; 

        for(long long i = 0; i<n; i++)
        {
            long long x;
            cin >> x; 
            arr.push_back(x); 
        }
        Solution ob;
        ob.reverseInGroups(arr, n, k);
        
        for(long long i = 0; i<n; i++){
            cout << arr[i] << " "; 
        }
        cout << endl;
    }
    return 0;
}


// } Driver Code Ends