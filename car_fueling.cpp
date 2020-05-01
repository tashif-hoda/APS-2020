#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    // write your code here
    int currfuel = tank;
    int refill=0;
    stops.push_back(dist);
    for(int i=0; i<stops.size()-1; i++)
    {
        if(stops[i+1] - stops[i] > tank)
            return -1;
        if(stops[i+1] - stops[i] <= currfuel)
            currfuel-=stops[i+1]-stops[i];
        else currfuel = tank - stops[i+1]+stops[i], refill++;
    }
    // for(auto i=stops.begin(); i!=stops.end(); i++) cout<<*i<<' ';
    return refill;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n+1);
    stops[0] = 0;
    for (size_t i = 1; i < n+1; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
