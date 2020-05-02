#include<bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);
#define endl "\n"
using namespace std;
  
int main() 
{ 
    string s;
    cin>>s;
    int hz=0, h1=0;
    bool flag=false;
    for(auto const& c:s)
    {
        if(c=='1')
        {
            h1++;
            hz=0;
        }
        if(c=='0')
        {
            hz++;
            h1=0;
        }

        if(h1>6 or hz>6)
        {
            flag = true;
            break;
        }
    }

    if(flag)
        cout<<"YES";
    else
        cout<<"NO";

    return 0; 
}
