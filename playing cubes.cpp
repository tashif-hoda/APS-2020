#include<bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);
using namespace std;
  
int main() 
{ 
    fastIO
    int n,m;
    cin>>n>>m;
    if(m>n)
        swap(n,m);
    cout<<n-1<<" "<<m;

    return 0; 
}
