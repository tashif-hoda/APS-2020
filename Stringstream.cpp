#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    int a, b, c, count=1;
    char ch;
    for(int i=0; i<str.size(); i++) if(str[i]==',') count+=1;
    // cout<<count<<endl;
    vector<int> ret;
    stringstream ss(str);
    for(int i=0; i<count; i++)
    {
        ss>>a>>ch;
        // cout<<a<<endl;
        ret.push_back(a);
        // ret.push_back(b);
        // ret.push_back(c);
    }
    return ret;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
