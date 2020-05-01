#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <cassert>
using std::vector;

long long get_fibonacci_partial_sum_naive(long long from, long long to) {
    long long sum = 0;

    long long current = 0;
    long long next  = 1;

    if(from>to)
    {
        int temp = to;
        to = from;
        from = temp;
    }

    for (long long i = 0; i <= to; ++i) {
        if (i >= from) {
            sum += current;
        }

        long long new_current = next%10;
        next = (next + current)%10;
        current = new_current%10;
    }

    return sum % 10;
}

int fibonacci_sum_fast(long long n) {
    if (n <= 1)
        return n;
    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous%10;
        previous = current%10;
        current = (tmp_previous + current)%10;
        sum += current;
        sum%=10;
    }
    return sum;
}

long long get_fibonacci_partial_sum_fast(long long from, long long to, vector<int>&v) {
    long long sum = 0;
    from%=300;
    to%=300;
    if(from>to)
    {
        // sum = 1;
        // for(int i=from; i<v.size(); i++){
        //     sum+=v[i];
        //     sum%=100;
        // }
        // for(int i=0; i<=to; i++){
        //     sum+=v[i];
        //     sum%=100;
        // }
        // return sum%10;
        int temp = from;
        from = to;
        to = temp;
    }
    long long current = 0;
    long long next  = 1;

    for (long long i = 0; i <= to; ++i) {
        if (i >= from) {
            sum += current%100;
        }

        long long new_current = next%100;
        next = (next + current)%100;
        current = new_current%100;
    }

    return sum % 10;
}

int main() {
    // while(true)
    // {
    // long long from = rand()%61, to = rand()%61;
    long long from, to;
    vector <int> v={0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 44, 33, 77, 10, 87, 97, 84, 81, 
                    65, 46, 11, 57, 68, 25, 93, 18, 11, 29, 40, 69, 9, 78, 87, 65, 52, 17, 69, 
                    86, 55, 41, 96, 37, 33, 70, 3, 73, 76, 49, 25, 74, 99, 73, 72, 45, 17, 62, 
                    79, 41, 20, 61, 81, 42, 23, 65, 88, 53, 41, 94, 35, 29, 64, 93, 57, 50, 7, 
                    57, 64, 21, 85, 6, 91, 97, 88, 85, 73, 58, 31, 89, 20, 9, 29, 38, 67, 5, 72, 
                    77, 49, 26, 75, 1, 76, 77, 53, 30, 83, 13, 96, 9, 5, 14, 19, 33, 52, 85, 37, 
                    22, 59, 81, 40, 21, 61, 82, 43, 25, 68, 93, 61, 54, 15, 69, 84, 53, 37, 90, 
                    27, 17, 44, 61, 5, 66, 71, 37, 8, 45, 53, 98, 51, 49, 0, 49, 49, 98, 47, 45, 
                    92, 37, 29, 66, 95, 61, 56, 17, 73, 90, 63, 53, 16, 69, 85, 54, 39, 93, 32, 
                    25, 57, 82, 39, 21, 60, 81, 41, 22, 63, 85, 48, 33, 81, 14, 95, 9, 4, 13, 17,
                    30, 47, 77, 24, 1, 25, 26, 51, 77, 28, 5, 33, 38, 71, 9, 80, 89, 69, 58, 27, 
                    85, 12, 97, 9, 6, 15, 21, 36, 57, 93, 50, 43, 93, 36, 29, 65, 94, 59, 53, 12, 
                    65, 77, 42, 19, 61, 80, 41, 21, 62, 83, 45, 28, 73, 1, 74, 75, 49, 24, 73, 97, 
                    70, 67, 37, 4, 41, 45, 86, 31, 17, 48, 65, 13, 78, 91, 69, 60, 29, 89, 18, 7, 
                    25, 32, 57, 89, 46, 35, 81, 16, 97, 13, 10, 23, 33, 56, 89, 45, 34, 79, 13, 92, 5, 97, 2, 99, 1,};
    std::cin >> from >> to;
    // std::cout << get_fibonacci_partial_sum_naive(from, to) << '\n';
    std::cout << get_fibonacci_partial_sum_fast(from, to, v) << '\n';
    // std::cout << from << " " <<to<<'\n';
    // assert(get_fibonacci_partial_sum_naive(from, to) == get_fibonacci_partial_sum_fast(from, to, v));
    // }
    return 0;
}
