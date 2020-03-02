#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

int arr[1000005];
int tree[4000020];

int minof(int a, int b)
{
    return (a<b)?a:b;
}

int mid(int s, int e)
{
    return (s+e)/2;
}

void build(int node, int start, int end)
{
    if(start==end)
    {
        tree[node]=arr[start];
    }
    else
    {
        int m=mid(start, end);
        build(2*node, start, m);
        build(2*node+1, m+1, end);
        tree[node]=minof(tree[2*node], tree[2*node+1]);
    }
}

int query(int node, int start, int end, int l, int r)
{
    if(r<start || l>end)
        return INT_MAX;
    
    if(l<=start && r>=end)
        return tree[node];
    
    int m = mid(start, end);
    int p1 = query(2*node, start, m, l, r);
    int p2 = query(2*node+1, m+1, end, l, r);
    return minof(p1,p2);
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,m, l, r, min;
    scanf("%d%d", &n, &m);
    int i, j;
    
    for(i=0; i<n; i++)
        scanf("%d", &arr[i]);
    
    build(1,0,n-1);
    // for(i=0;i<4*n;i++)            //print array
    //     printf("%d ",tree[i]);
    // printf("\n");
    for(i=0; i<m; i++)
    {
        scanf("%d%d", &l, &r);
        int q=query(1,0,n-1,l,r);
        printf("%d\n", q);
    }
    //printf("%d %d", n, m);
    
    return 0;
}
