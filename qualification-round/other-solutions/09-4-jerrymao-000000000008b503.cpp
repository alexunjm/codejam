#include <bits/stdc++.h>
using namespace std;

void extend(vector<int> &a, vector<int> b) { a.insert(a.end(), b.begin(), b.end()); }

vector<int> slv(string res[5], int lo, int hi, int st, int lv)
{
	assert(lv >= -1);
	vector<int> ans;
	if (hi-lo == (1<<(lv+1))) return ans;
	if (lo == hi)
	{
		for (int i = 0;i < (1<<(lv+1));i++) ans.push_back(st+i);
		return ans;
	}
	int i = lo;
	while (i < hi && res[lv][i] == '0') i++;
	extend(ans, slv(res, lo, i, st, lv-1));
	extend(ans, slv(res, i, hi, st+(1<<lv), lv-1));
	return ans;
}

void solve()
{
	int n, b, f; cin >> n >> b >> f;
	string res[5];
	for (int i = 0;i < 5;i++)
	{
		string q;
		for (int j = 0;j < n;j++) q.push_back('0'+!!(j&(1<<i)));
		cout << q << endl;
		cin >> res[i];
		for (int j = n;j&32;j++) res[i].push_back('0'+!!(j&(1<<i)));
	}
	while (n&32) n++;
	vector<int> ans;
	int state = 0, from = 0, actual = 0;
	for (int i = 0;i < n-b;i++)
		if (res[4][i] == '1') state = 1;
		else if (state == 1)
		{
			extend(ans, slv(res, from, i, actual, 4));
			state = 0, from = i, actual += (1<<5);
		}
	extend(ans, slv(res, from, n-b, actual, 4));
	for (int i = 0;i < b;i++)
	{
		cout << ans[i];
		if (i != b-1) cout << ' ';
	}
	cout << endl;
	int blah; cin >> blah;
	if (blah == -1) exit(0);
}

int main()
{
	int t; cin >> t;
	for (int _ = 1;_ <= t;_++) solve();
	return 0;
}
