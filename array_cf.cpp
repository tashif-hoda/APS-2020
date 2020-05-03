#include<bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;

int main()
{
    fastIO
    int n, temp;
    vector <int> v, seta, setb, setc;
    cin>>n;
    for(int i=0; i<n; i++)
    {
        cin>>temp;
        v.push_back(temp);
    }
    
    for(int i=0; i<n; i++)
    {
        if(v[i]==0)
            setc.push_back(0);
        
        else if(v[i]<0)
            seta.push_back(v[i]);
        
        else
            setb.push_back(v[i]);
    }
    
    if(!(seta.size()&1))
    {
        int neg = seta.back();
        seta.pop_back();
        setc.push_back(neg);
        
    }
    
    if(setb.empty())
    {
        setb.push_back(seta.back());
        seta.pop_back();
        setb.push_back(seta.back());
        seta.pop_back();
    }
    
    cout<<seta.size()<<" "; for(auto it=seta.begin(); it!=seta.end(); it++) cout<<*it<<" ";cout<<"\n";
    cout<<setb.size()<<" "; for(auto it=setb.begin(); it!=setb.end(); it++) cout<<*it<<" ";cout<<"\n";
    cout<<setc.size()<<" "; for(auto it=setc.begin(); it!=setc.end(); it++) cout<<*it<<" ";cout<<"\n";
    return 0;
}
