#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int tonum(char arr[]) {
	int res = 0;
	for (int i = 0; arr[i]; i++) {
		res *= 10;
		res += arr[i] - '0';
	}
	return res;
}

int conv(int num, int l, int r) {
	// l과 r의 체크가 안되어있음
	// 처음에 num의 자리수는 정해져있기때문에 그걸 이용하면  됨
	// arr
	char buf[16];
	sprintf(buf, "%d", num);
	char tmp;
	// swap
	tmp = buf[l];
	buf[l] = buf[r];
	buf[r] = tmp;
	// 앞자리가 0이 아닌지 체크도..
	if (buf[0] == '0') return 0;
	return tonum(buf);
}

int n, k;

bool isok(int num) {
	// 예외가 되는 것들은 바로처리
	// 1 ~ 9 ==> 교환이 안됨 ==> -1
	if (num < 10) return false;
	// 10, 20, .. .90 ==> 교환이 안됨 ==> -1
	if (num < 100 && num % 10 == 0) return false;
	return true;
}

int get_num_len(int num) {
	int len = 0;
	while (num > 0) {
		len++;
		num /= 10;
	}
	return len;
}

int main_exchange() {
	// todo - 완전탐색
	// 숫자를 직접 교환하는 로직
	// 교환해서 단계별로 탐색해가는 로직
	// 그리고 답 구하면 됨
	scanf("%d%d", &n, &k);
	if (n == 1000000) {
		printf("%d", n);
		return 0;
	}
	if (!isok(n)) {
		printf("-1");
		return 0;
	}

	queue<int> q;
	q.push(n);

	for (int i = 0; i < k; i++) {
		// q --> next_q --> q
		// 단계별로 처리하기 위해서
		// 다음번 작업을 하기전에 임시로 저장하는 곳이고
		// q size를 이용해서 어찌어찌 처리를 하면 필요가 없어요 ==> 고민해보시면 됨
		vector<int> next_q;

		while (!q.empty()) {
			int cur = q.front();
			q.pop();
			int len = get_num_len(cur);
			printf("%d\n", cur);

			for (int s = 0; s < len; s++) {
				for (int e = s + 1; e < len; e++) {
					int next_num = conv(cur, s, e);
					if (next_num == 0) continue;
					// 꼭 다 넣어야할까????
					// 현재 다음번 처리는 "중복"이 발생하고 있습니다
					// 적절하게 처리해 중복을 피해봅시다
					next_q.push_back(next_num);
				}
			}
		}

		for (int i = 0; i < next_q.size(); i++) {
			q.push(next_q[i]);
		}
	}
	// k번을 돌렸기 때문에 q에남아 있는 것들은 k번을 수행하고 남은 숫자들이고
	// q에 남은것 중에 가장 큰것을 출력하면 됨
	int ans = 0;
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		if (ans < cur) ans = cur;
	}
	printf("%d", ans);
}