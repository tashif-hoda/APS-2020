#include <iostream>
#include <vector>
// using namespace std;

// long long get_fibonacci_huge_naive(long long n, long long m) {
//     if (n <= 1)
//         return n;

//     long long previous = 0;
//     long long current  = 1;

//     for (long long i = 0; i < n - 1; ++i) {
//         long long tmp_previous = previous;
//         previous = current;
//         current = tmp_previous + current;
//     }

//     return current % m;
// }

// int get_fibonacci_last_digit(int n) {
//     if (n <= 1)
//         return n;

//     int previous = 0;
//     int current  = 1;

//     for (int i = 0; i < n - 1; ++i) {
//         int tmp_previous = previous%4100;
//         previous = current%4100;
//         current = tmp_previous + current%4100;
//     }
//     return current%4100;
// }

long long get_fibonacci_huge_fast(long long n, long long m, std::vector<int>& v) {
    if (n <= 1)
    {
        v.push_back(1);
        v.push_back(0);
        return n;
    }
    int previous = 0;
    int current  = 1;
    v.push_back(previous);
    v.push_back(current);
    for (long long int i = 1; i < n; ++i) {
        int tmp_previous = previous%m;
        previous = current%m;
        current = (tmp_previous + current)%m;
        v.push_back(current);
        if(previous==0 and current==1)
            return i;
    }
    return current;
}

int main() {
    long long n;
    int m;
    std::vector<int> v;
    std::cin >> n >> m;
    int period = get_fibonacci_huge_fast(n, m, v);
    if (v[v.size()-1]!=1 || v[v.size()-2]!=0)
        std::cout<< period <<'\n';
    else
        std::cout<< v[n%period]%m <<'\n';
    for(auto i=v.begin(); i!=v.end(); i++) std::cout<<*i<<", " ;
    std::cout<< '\n'<<period;
}
