#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

bool comp(const vector<double>& v1, const vector<double>& v2)
{
  return v1[2]>v2[2];
}

double get_optimal_value(int cap, vector<int>& weights, vector<int>& values) {
  double val = 0.0;

  // write your code here
  vector<vector<double>> vbyw;
  int n = weights.size();
  for(int i=0; i<n; i++)
  {
    vbyw.push_back({(double)weights[i], (double)values[i], ((double)values[i])/((double)weights[i])});
  }
  sort(vbyw.begin(), vbyw.end(), comp);

  // for(auto row = vbyw.begin(); row!=vbyw.end(); row++, std::cout<<'\n')
  //   for(auto col = row->begin(); col!=row->end(); col++)
  //     std::cout<<*col<<' ';

  int i=0;
  while(i<n && cap>0)
  {
    if(vbyw[i][0]<=cap)
    {
      cap-=vbyw[i][0];
      val+=vbyw[i][1]; 
    }
    else
    {
      val+=cap*vbyw[i][2];
      cap=0;
    }
    i++;
  }
  return val;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }
  double optimal_value = get_optimal_value(capacity, weights, values);
  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}