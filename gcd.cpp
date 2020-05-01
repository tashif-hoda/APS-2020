#include <iostream>
// #include <cassert>

int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}

long long int gcd_fast(long long int a, long long int b) {
  if(a==0||b==0)
    return a;
  return gcd_fast(b, a%b);
}

int main() {
  long long int a, b;
  std::cin >> a >> b;
  // std::cout << gcd_naive(a, b) << std::endl;
  std::cout << gcd_fast(a, b) << std::endl;
  // assert(gcd_fast(a, b) == gcd_naive(a, b));
  return 0;
}
