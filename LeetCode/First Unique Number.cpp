class FirstUnique {
    public:
    unordered_map<int, pair<list<int>::iterator, bool>> hashmap;
    list<int> l;
    FirstUnique(vector<int>& nums) {
    for(auto it=nums.begin(); it!=nums.end(); it++)
        add(*it);
    }

    int showFirstUnique() {
        if (l.empty())
            return -1;
        return l.back();
    }

    void add(int value) {
        unordered_map<int, pair<list<int>::iterator, bool>>::iterator it = hashmap.find(value);
        if(it == hashmap.end())
        {
            l.push_front(value);
            hashmap[value] = make_pair(l.begin(), false) ;
        }

        else
        {
            if((it->second).second == false)
            {
                l.erase((it->second).first);
                (it->second).second = true;
            }
        } 
    }
 };
