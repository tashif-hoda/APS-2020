#include<bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);
#define endl "\n"
#define get getchar_unlocked
// #define put putchar_unlocked
// #define int long long
using namespace std;
void intscan(int &num){bool n=false;register int c; num = 0; c=get();if(c=='-'){n = true;c = get();} for(;(c>47&&c<58);c=get())num=num*10+c-48; if(n) num*=-1;} 
  
int main() 
{
    fastIO
    int t, n, c, a[100005];
    intscan(t);
    while(t--)
    {
        intscan(n);
        intscan(c);
        for(int i=0; i<n; i++) intscan(a[i]);
        sort(a, a+n);
        int ans;
        int l=0, h=100000000, mid;
        while (l<=h)
        {
            mid = l + (h-l)/2;
            int f = a[0], count=1;
            for(int i=1; i<n; i++)
            {
                if(a[i]-f>=mid)
                {
                    count++;
                    f = a[i];
                }
            }
            
            if(count<c)
                h = mid-1;
            else
            {
            	ans = mid;
                l = mid+1;
            }
        }
        
        cout<<ans<<endl;
    }
    return 0; 
} 
