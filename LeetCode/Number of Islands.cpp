class Solution {
public:
    
    int findparent(int v, int parent[])
    {
        if(v==parent[v])
            return v;
        parent[v] = findparent(parent[v], parent);
        return parent[v];
    }
    
    void join(int a, int b, int parent[], int size[])
    {
        a = findparent(a, parent);
        b = findparent(b, parent);
        
        if(b!=a)
        {
            if (size[a]<size[b])
            {
                swap(a,b);
            }
                
            parent[b] = a;
            size[a]+=size[b];
        }
    }
    
    int numIslands(vector<vector<char>>& grid) {
        if(grid.empty())
            return 0;
        int l = grid.size();
        int b = grid[0].size();
        
        int *parent= new int[l*b+5];
        int *size= new int[l*b+5];
        vector <vector<int>> idx;
        for(int i=1; i<l*b+1; i++)
        {
            if(grid[(i-1)/b][(i-1)%b]!='0')
            {
                parent[i]=i;
                idx.push_back({(i-1)/b, (i-1)%b});
            }
            else
                parent[i]=0;
            size[i]=1;
        }
        
        while(!idx.empty())
        {

            int i=idx.back()[0], j=idx.back()[1];
            idx.pop_back();
            if(i<l-1)
            {
                if(grid[i+1][j]=='1')
                    join(i*b+j+1, (i+1)*b+j+1, parent, size);
            }
            if(j<b-1)
            {
                if(grid[i][j+1]=='1')
                    join(i*b+j+1, i*b+(j+1)+1, parent, size);
            }
            if(i>0)
            {
                if(grid[i-1][j]=='1')
                    join(i*b+j+1, (i-1)*b+j+1, parent, size);
            }
            if(j>0)
            {
                if(grid[i][j-1]=='1')
                    join(i*b+j+1, i*b+(j-1)+1, parent, size);
            }
        }
        
        unordered_set <int> s;
        for(int i=1; i<l*b+1; i++)
            if(parent[i]!=0) s.insert(findparent(i, parent));
        delete[] parent;
        delete[] size;
        return s.size();
        
    }
};
