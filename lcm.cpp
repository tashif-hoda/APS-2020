#include <iostream>
#include <cassert>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long int gcd_fast(int a, int b) {
  if(a==0||b==0)
    return a;
  return gcd_fast(b, a%b);
}

long long lcm_fast(long long int a, long long int b) {
  return (a*b)/gcd_fast(a,b);
}

int main() {
  int a, b;
  std::cin >> a >> b;
  // std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm_fast(a, b) << std::endl;
  // assert(lcm_fast(a, b) == lcm_naive(a, b));
  return 0;
}
