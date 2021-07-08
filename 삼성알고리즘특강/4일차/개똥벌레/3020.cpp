/*
#include <cstdio>

int n, h, answer, count;
int seok[200000], jong[200000];

// x 구간으로 날아갈 때 k번째 석순과 만나는지
bool check_seok(int k, int x) {
	if (x <= seok[k]) return true;
	return false;
}

// x 구간으로 날아갈 때 k번째 종유석과 만나는지
bool check_jong(int k, int x) {
	if (x >= h - jong[k] + 1) return true;
	return false;
}

int fly(int x) {
	int res = 0;
	for (int i = 0; i < n; i += 2) {
		// 석순과 만나는지
		if (check_seok(i, x)) res++;
		// 종유석과 만나는지
		if (check_jong(i, x)) res++;
	}
	return res;
}

int main() {
	scanf("%d %d", &n, &h);
	for (int i = 0; i < n; i += 2) {
		scanf("%d", &seok[i]);
		scanf("%d", &jong[i]);
	}
	answer = -1;
	for (int i = 1; i <= h; i++) {
		int crash = fly(i);
		if (answer == -1 || crash < answer) {
			answer = crash;
			count = 1;
		}
		else if (crash == answer) {
			count++;
		}
	}
	printf("%d %d", answer, count);
}*/

// 이분탐색으로 하기에는 결과 값의 증감이 일정하지 않고 이 문제는 count를 세어야 하기 때문에 적절하지 못하다

// 완전 탐색으로 하기에는 시간이 오래 걸린다.
// 구간에서 만나는 판단을 빠르게 할 수 없을까?
// 구간트리 문제에서도 많이 사용
// 1. 정렬하고 누적시킴
// 2. +1, -1 .....

#include <cstdio>

int n, h, answer, count;
int sum[500010];

int main() {
	scanf("%d %d", &n, &h);
	for (int i = 0; i < n; i++) {
		int bar;
		scanf("%d", &bar);
		if (i & 1) {
			// 종유석
			sum[h - bar + 1]++;
		}
		else {
			// 석순
			sum[1]++;
			sum[bar + 1]--;
		}
	}
	answer = -1;
	for (int i = 1; i <= h; i++) {
		sum[i] += sum[i - 1];
		if (answer == -1 || sum[i] < answer) {
			answer = sum[i];
			count = 1;
		}
		else if (sum[i] == answer) {
			count++;
		}
	}

	printf("%d %d", answer, count);
}