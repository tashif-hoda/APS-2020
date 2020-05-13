//code sourced from https://www.geeksforgeeks.org/count-sub-arrays-whose-product-is-divisible-by-k/
#include <bits/stdc++.h>
#define ll long long int
#define MAX 100005 
#define pb push_back
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std; 

int cnts[MAX];

ll countSubarrays(int* arr, int n) 
{ 
    ll curr_map=0;  
    ll k=1;
    
    int l = 0, r = 0; 
    ll ans = 0; 
    while (r < n) { 
        
        if (arr[r]%2==0)
        {
            if (arr[r]==0)
                arr[r]=4;
            curr_map+=ceil(log2((arr[r] & (~(arr[r] - 1)))));
            cnts[r]+=ceil(log2((arr[r] & (~(arr[r] - 1)))));
            arr[r]=1;
        }
         
        if (curr_map < 2)
        { 
            r++; 
        } 
  
        else 
        { 
            ans += n - r; 
            curr_map -= cnts[l]; 
            l++; 
        } 
    } 
  
    return ans; 
} 

ll countcontOdd(int* arr, int n)
{
    ll rs=0, codd=0;
    for(int i=0; i<n; i++)
    {
        if(arr[i]&1)
        {
            codd++;
        }
        else
        {
            rs+=((codd)*(codd+1))/2;
            codd=0;
        }
    }
    rs+=((codd)*(codd+1))/2;
    return rs;
}

int main()
{
    fastIO
    int t, n;
    int arr[100005];
    ll count4, countodd;
    memset(arr, 0, sizeof(arr));
    cin>>t;
    while(t--)
    {
        memset(arr, 0, sizeof(arr));
        memset(cnts, 0, sizeof(cnts));
        cin>>n;
        for(int i=0; i<n; i++) cin>>arr[i];
        countodd=countcontOdd(arr, n);
        count4=countSubarrays(arr, n);
        cout<<countodd+count4<<"\n";
    }
    
    return 0;
}
