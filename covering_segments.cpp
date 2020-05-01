#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using std::vector;

struct Segment {
  int start, end;
};

bool comp(const Segment& seg1, const Segment& seg2)
{
  if(seg1.start+seg1.end != seg2.start + seg2.end)
    return seg1.start+seg1.end < seg2.start + seg2.end;
  else
    return seg1.start < seg2.start;
}

vector<int> optimal_points(vector<Segment> &segments) {
  vector<int> points;
  //write your code here
  sort(segments.begin(), segments.end(), comp);

  // for(auto itr = segments.begin(); itr!=segments.end(); itr++, std::cout<<"\n")
  //   std::cout<<(*itr).start<<" "<<(*itr).end;

  int i=0;
  int st = segments[i].start, en = segments[i].end;
  while(++i<segments.size())
  {
    if(segments[i].start<=en and segments[i].end>=en)
      continue;
    if(segments[i].end<en)
      en = segments[i].end;
    else
    {
      points.push_back(en);
      en = segments[i].end;
    }
  }
  points.push_back(en);
  return points;
}

int main() {
  int n;
  std::cin >> n;
  vector<Segment> segments(n);
  for (size_t i = 0; i < segments.size(); ++i) {
    std::cin >> segments[i].start >> segments[i].end;
  }
  vector<int> points = optimal_points(segments);
  std::cout << points.size() << "\n";
  for (size_t i = 0; i < points.size(); ++i) {
    std::cout << points[i] << " ";
  }
}
