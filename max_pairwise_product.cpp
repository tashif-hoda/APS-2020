#include <iostream>
#include <vector>
#include <algorithm>

// int MaxPairwiseProduct(const std::vector<int>& numbers) {
//     int max_product = 0;
//     int n = numbers.size();

//     for (int first = 0; first < n; ++first) {
//         for (int second = first + 1; second < n; ++second) {
//             max_product = std::max(max_product,
//                 numbers[first] * numbers[second]);
//         }
//     }

//     return max_product;
// }

long long MaxPairwiseProduct(const std::vector<int>& nums) {
    int n = nums.size();
    long long int m1=-999999, m2=-999999, mi=0;
    for(int i = 0; i < n; i++) {
        if(nums[i]>m1)
            m1=nums[i], mi=i;
    }
    for(int i=0; i<n; i++)
    {
        if(nums[i]>m2 && i!=mi)
            m2 = nums[i];
    }
    return m1*m2;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProduct(numbers) << "\n";
    return 0;
}
