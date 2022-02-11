/*
문제
자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 n (1 ≤ n ≤ 1012)이 주어진다.

출력
GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 출력한다.

예제 입력 1
1
예제 출력 1
1
예제 입력 2
5
예제 출력 2
4
예제 입력 3
10
예제 출력 3
4
예제 입력 4
45
예제 출력 4
24
예제 입력 5
99
예제 출력 5
60
*/

#include<iostream>
#include<cmath>
#include<string>
#include<vector>
using namespace std;
#define ll long long int

int main() {
	ll n; 
	cin >> n;					//정수 범위가 크기 때문에 ll 사용
	ll Euler = n;

	//오일러 피함수는 양의 정수 n에 대해서 1~n-1사이의 
	//서로소의 개수를 찾는 알고리즘
	//문제를 풀기 위해서 기존의 gcd알고리즘을 쓰면 시간초과 남
	//그래서 오일러 피함수 사용
	//수식 https://ko.wikipedia.org/wiki/%EC%98%A4%EC%9D%BC%EB%9F%AC_%ED%94%BC_%ED%95%A8%EC%88%98 참조

	for (ll i = 2; i * i <= n; i++) {
		if (n % i == 0) {
			Euler /= i;
			Euler *= (i - 1);
		}
		while (n % i == 0) n /= i;
	}
	if (n != 1) {
		Euler /= n;
		Euler *= (n - 1);
	}
	cout << Euler;
}