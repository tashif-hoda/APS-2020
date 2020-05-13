#include<bits/stdc++.h>
#include<stdio.h>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);
#define endl "\n"
// #define get getchar_unlocked
// #define put putchar_unlocked
using namespace std;
// void intscan(int &num)
// {
//     bool n=false;register int c; num = 0; c=getchar();if(c=='-'){n = true;c = getchar();} for(;(c>47&&c<58);c=getchar())num=num*10+c-48; if(n) num*=-1;
    
// } 
  
int main() 
{ 
    fastIO
    int d, n, *a;
    cin>>d>>n;
    a = new int[n];
    for(int i=0; i<n; i++) cin>>a[i];
    int nc=0;
    for(int i=1; i<n; i++)
        nc+=d-a[i-1];
    delete[] a;
    cout<<nc;
    return 0; 
}
