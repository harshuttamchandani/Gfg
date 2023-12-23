//{ Driver Code Starts
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    int minValueToBalance(int a[], int n)
    {
       //code here.
       int mid= n/2;
       int s1=0;
       int s2=0;
     
       for(int i=0;i<n;i++)
       {
           if(i<mid)
           {
               s1=s1+a[i];
           }
           else
           {
               s2=s2+a[i];
           }
       }
       int ans=abs(s1-s2);
       return ans;
       
    }
};



//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int a[n];
		for(int i=0;i<n;++i)
			cin>>a[i];
		Solution ob;	
		cout<<ob.minValueToBalance(a,n)<<endl;
	}
	return 0;
}
// } Driver Code Ends