#include<iostream>
#include<cmath>
#include<string>
using namespace std;
long long int dp[101] = { 1,1,1, };

int main() {
	int n;
	int i;
	int x;
	cin >> x;
	while (x) {
		x--;
		cin >> n;
		for (i = 3; i < n; i++) {
			dp[i] = dp[i - 2] + dp[i - 3];
		}
		cout << dp[n - 1] << endl;
	}
}