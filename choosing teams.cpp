#include <iostream>
#include<bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define ll long long
using namespace std;

int main()
{
    fastIO
    int n,k, temp;
    cin>>n>>k;
    vector <int> v;
    for(int i=0; i<n; i++)
    {
        cin>>temp;
        v.push_back(temp);
    }
    
    sort(v.begin(), v.end());
    int i=0;
    for(i=0; i<n; i++)
    {
        if (v[i]>5-k)
        {
            break;
        }
    }
    
    if (i>2)
    {
        cout<<i/3<<endl;
    }
    else
    {
        cout<<0<<endl;
    }
    
    return 0;
}
