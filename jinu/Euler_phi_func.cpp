/*
����
�ڿ��� n�� �־����� ��, GCD(n, k) = 1�� �����ϴ� �ڿ��� 1 �� k �� n �� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù° �ٿ� �ڿ��� n (1 �� n �� 1012)�� �־�����.

���
GCD(n, k) = 1�� �����ϴ� �ڿ��� 1 �� k �� n �� ������ ����Ѵ�.

���� �Է� 1
1
���� ��� 1
1
���� �Է� 2
5
���� ��� 2
4
���� �Է� 3
10
���� ��� 3
4
���� �Է� 4
45
���� ��� 4
24
���� �Է� 5
99
���� ��� 5
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
	cin >> n;					//���� ������ ũ�� ������ ll ���
	ll Euler = n;

	//���Ϸ� ���Լ��� ���� ���� n�� ���ؼ� 1~n-1������ 
	//���μ��� ������ ã�� �˰���
	//������ Ǯ�� ���ؼ� ������ gcd�˰����� ���� �ð��ʰ� ��
	//�׷��� ���Ϸ� ���Լ� ���
	//���� https://ko.wikipedia.org/wiki/%EC%98%A4%EC%9D%BC%EB%9F%AC_%ED%94%BC_%ED%95%A8%EC%88%98 ����

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