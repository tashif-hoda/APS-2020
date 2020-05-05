#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n, q, num;
    int queue[100005];
    int fr=0, re=0;
    cin>>n;
    while (n--)
    {
        cin>>q;
        if (q==1)
        {
            cin>>num;
            queue[fr]=num;
            fr++;
        }
        else if(q==2)
        {
            if (re<fr)
            {
                // queue[re]=0;
                re++;
            }
        }

        else
        {
            cout<<queue[re]<<"\n";
        }
        // for(int i=0; i<10; i++) cout<<queue[i]<<" ";
    }
    return 0;
}
