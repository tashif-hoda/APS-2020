#include<bits/stdc++.h>
#define fastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define BLOCK 170
using namespace std;
 
bool comp(const vector<int>&x,const vector <int>&y) 
{ 
    if (x[0]/BLOCK != y[0]/BLOCK) 
        return x[0]/BLOCK < y[0]/BLOCK;
  
    return x[1]<y[1]; 
} 
 
 
int main() {
    fastIO
	int n, m, arr[30005], l,r, res[200005];
	vector<vector<int>> qu;
	cin>>n;
	for(int i=0;i<n;i++) cin>>arr[i];
// 	for(int i=0;i<n;i++) cout<<arr[i];
	cin>>m;
	for(int i=0; i<m; i++)
	{
	    cin>>l>>r;
	    qu.push_back({l,r,i});
	}
	sort(qu.begin(), qu.end(), comp);
	unordered_map <int, int> umap;
	int st=0, en=-1;
	for(int i=0; i<m; i++)
	{
	    l=qu[i][0]-1;
	    r=qu[i][1]-1;
	    while (l<st)
	    {
	        st--;
	        if (umap.find(arr[st])==umap.end())
	        {
	            umap.insert(make_pair(arr[st], 1));
	        }
	        else
	            umap[arr[st]]++;
	    }
	    while (en<r)
	    {
	        en++;
	        if (umap.find(arr[en])==umap.end())
	        {
	            umap.insert(make_pair(arr[en], 1));
	        }
	        else
	            umap[arr[en]]++;
	       //cout<<ar
	    }
	    
	    while (l>st)
	    {
            umap[arr[st]]--;
            if (umap[arr[st]]==0)
                umap.erase(arr[st]);
	        st++;
	    }
	    while (r<en)
	    {
            umap[arr[en]]--;
            if (umap[arr[en]]==0)
                umap.erase(arr[en]);
	        en--;
	    }
	   // cout<<umap.size()<<" ";
	    res[qu[i][2]]=umap.size();
	    
	}
	    
	for(int i=0; i<m; i++) cout<<res[i]<<"\n";
	
	return 0;
} 
