#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

using Int = long long;

template <class T1, class T2> ostream &operator<<(ostream &os, const pair<T1, T2> &a) { return os << "(" << a.first << ", " << a.second << ")"; };
template <class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cerr << *i << " "; cerr << endl; }
template <class T> void chmin(T &t, const T &f) { if (t > f) t = f; }
template <class T> void chmax(T &t, const T &f) { if (t < f) t = f; }


int N, B, F;
char result[1030];

int main() {
  int numCases;
  scanf("%d", &numCases);
  for (int caseId = 1; caseId <= numCases; ++caseId) {
    cerr << "==== Case #" << caseId << " ====" << endl;
    scanf("%d%d%d", &N, &B, &F);
    cerr << "N = " << N << ", B = " << B << endl;
    
    string query(N, '?');
    int pos;
    
    for (int i = 0; i < N; ++i) {
      query[i] = "01"[i % 32 / 16];
    }
    printf("%s\n", query.c_str());
    fflush(stdout);
    scanf("%s", result);
    cerr << "query " << query << ": " << result << endl;
    
    vector<int> xs;
    for (int i = 0; i <= N; i += 16) {
      xs.push_back(i);
    }
    if (xs.back() < N) {
      xs.push_back(N);
    }
    int len = (int)xs.size() - 1;
    vector<int> bs;
    pos = 0;
    for (int j = 0; j < N / 16; ++j) {
      int cnt = 0;
      for (; pos < N - B && result[pos] == "01"[j % 2]; ++pos) {
        ++cnt;
      }
      bs.push_back(16 - cnt);
    }
    if ((int)bs.size() < len) {
      int bb = B;
      for (const int b : bs) {
        bb -= b;
      }
      bs.push_back(bb);
    }
// cerr<<"len = "<<len<<endl;
// cerr<<"xs = ";pv(xs.begin(),xs.end());
// cerr<<"bs = ";pv(bs.begin(),bs.end());
    
    for (int iter = 0; iter < 4; ++iter) {
      for (int k = 0; k < len; ++k) {
        const int mid = (xs[k] + xs[k + 1]) / 2;
        for (int x = xs[k]; x < xs[k + 1]; ++x) {
          query[x] = "01"[(x < mid) ? 0 : 1];
        }
      }
      printf("%s\n", query.c_str());
      fflush(stdout);
      scanf("%s", result);
      cerr << "query " << query << ": " << result << endl;
      
      vector<int> xsNext;
      for (int k = 0; k < len; ++k) {
        const int mid = (xs[k] + xs[k + 1]) / 2;
        xsNext.push_back(xs[k]);
        xsNext.push_back(mid);
      }
      xsNext.push_back(N);
      const int lenNext = (int)xsNext.size() - 1;
      vector<int> bsNext;
      pos = 0;
      for (int k = 0; k < len; ++k) {
        const int mid = (xs[k] + xs[k + 1]) / 2;
        int cnt0 = 0, cnt1 = 0;
        for (int l = 0; l < (xs[k + 1] - xs[k]) - bs[k]; ++l) {
          (result[pos++] == '0') ? ++cnt0 : ++cnt1;
        }
// cerr<<"  "<<xs[k]<<" "<<mid<<" "<<xs[k+1]<<": "<<cnt0<<" "<<cnt1<<endl;
        bsNext.push_back((mid - xs[k]) - cnt0);
        bsNext.push_back((xs[k + 1] - mid) - cnt1);
      }
      
      len = lenNext;
      xs = xsNext;
      bs = bsNext;
// cerr<<"len = "<<len<<endl;
// cerr<<"xs = ";pv(xs.begin(),xs.end());
// cerr<<"bs = ";pv(bs.begin(),bs.end());
    }
    
    vector<int> ans;
    for (int k = 0; k < len; ++k) {
      if (bs[k]) {
        ans.push_back(xs[k]);
      }
    }
    assert((int)ans.size() == B);
    
    int ou = 0;
    for (const int i : ans) {
      if (ou++) {
        printf(" ");
      }
      printf("%d", i);
    }
    printf("\n");
    fflush(stdout);
    
    scanf("%s", result);
    cerr << "result = " << result << endl;
    if (!strcmp(result, "-1")) {
      break;
    }
  }
  return 0;
}
