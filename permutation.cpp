#include<bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define ll long long
using namespace std;

int main()
{
    fastIO
    int n, temp;
    cin>>n;
    set <int> s;
    int nc=0;
    for(int i=0; i<n; i++)
    {
        cin>>temp;
        s.insert(temp);
    }
    for(auto it=s.begin(); it!=s.end(); it++)
    {
        if(*it>n)
            nc++;
    }
    cout<<n-s.size()+nc;
    
    return 0;
}
