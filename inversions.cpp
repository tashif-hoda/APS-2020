#include <iostream>
#include <vector>

using namespace std;

long long merge(vector<int> &a, vector<int> &temp, int l, int mid, int h)
{
  long long n=0;
  int i=l, j=mid+1, pt=l;
  while (i<=mid && j<=h)
  {
    if(a[i] <= a[j])
      temp[pt++] = a[i++];
    else
    {
      temp[pt++] = a[j++];
      n+=j-pt;
    }
  }
  for(;i<=mid;)
    temp[pt++] = a[i++];
  for(;j<=h;)
    temp[pt++] = a[j++];
  for(i=l; i<=h; i++)
    a[i] = temp[i];
  return n;
}

long long bruteforce(vector<int> &a)
{
  long long inv=0;
  for (int i=0; i<a.size(); i++)
  {
    for(int j=i+1; j<a.size(); j++)
      if(a[i]>a[j])
        inv++;
  }
  return inv;
}

long long get_number_of_inversions(vector<int> &a, vector<int> &b, size_t left, size_t right, long long number_of_inversions) {
  if (left>=right) return number_of_inversions;
  size_t ave = left + (right - left) / 2;
  number_of_inversions = get_number_of_inversions(a, b, left, ave, number_of_inversions);
  number_of_inversions = get_number_of_inversions(a, b, ave+1, right, number_of_inversions);
  number_of_inversions+= merge(a, b, left, ave, right);
  return number_of_inversions;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  vector<int> b(a.size());
  long long y = get_number_of_inversions(a, b, 0, a.size()-1, 0);
  std::cout << y << '\n';
  return 0;
}
