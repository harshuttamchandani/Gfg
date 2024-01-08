//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
long long int maxSum(int arr[], int n);

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int arr[n];
		for(int i=0;i<n;++i)
			cin>>arr[i];
		cout<<maxSum(arr,n)<<endl;
	}
	return 0;
}
// } Driver Code Ends


long long int maxSum(int arr[], int n)
{
    sort(arr,arr+n);
    int i=0;
    int j=n-1;
    long long int sum=0;
    int a[n];
    int e=0;
    int o=1;
    while(i<=j)
    {
        a[e]=arr[i];
        a[o]=arr[j];
        i++;
        j--;
        //cout<<a[e]<<" "<<a[o]<<endl;
        e=e+2;
        o=o+2;
    }
    
    i=0;
    j=1;
    sum=a[n-1]-a[0];
    while(j<n)
    {
        sum=sum+abs(a[j]-a[i]);
        i++;
        j++;
        
    }
    return sum;
}