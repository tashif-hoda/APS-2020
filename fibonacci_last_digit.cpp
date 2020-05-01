#include <iostream>
#include <vector>
// #include <>
using namespace std;

vector<int> v;
long long int get_fibonacci_last_digit_naive(long long int n, long long int m) {
    if (n <= 1)
        return n;
    int previous = 0;
    int current  = 1;
    cout<<previous<<" "<<current<<" ";
    v.push_back(previous);
    v.push_back(current);
    for (int i = 1; i < n; ++i) {
        int tmp_previous = previous%m;
        previous = current%m;
        current = (tmp_previous + current)%m;
        cout<<current<<" ";
        v.push_back(current);
        if(previous==0 and current==1)
            return i;
    }
    cout<<"\n";
    return current;
}

int main() {
    long long n, m;
    std::cin >> n>>m;
    int c = get_fibonacci_last_digit_naive(n, m);
    std::cout <<'\n'<< c << '\n';
    return 0;
    }
