struct node
{
    int key;
    int value;
};

class LRUCache {
public:
    unordered_map<int, list<node>::iterator> hashmap;
    list<node> dll;
    int maxsize;
    
    LRUCache(int capacity) {
        maxsize = capacity;
    }
    
    int get(int key) {
        unordered_map<int, list<node>::iterator>::iterator it = hashmap.find(key);
        if(it != hashmap.end())
        {
            node n = *(it->second);
            dll.push_front(n);
            dll.erase(it->second);
            it->second = dll.begin();
            return n.value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        unordered_map<int, list<node>::iterator>::iterator it = hashmap.find(key);
        if(it!=hashmap.end())
        {
            node n = *(it->second);
            dll.erase(it->second);
            n.value = value;
            dll.push_front(n);
            it->second = dll.begin();
        }
        else
        {
            node n;
            n.key = key;
            n.value = value;
            dll.push_front(n);
            hashmap[key] = dll.begin();
            if(dll.size()>maxsize)
            {
                node n = dll.back();
                hashmap.erase(n.key);
                dll.pop_back();
            }
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
