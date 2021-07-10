#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

int n, h[50][50], dy[] = { -1, 1, 0, 0, -1, -1, 1, 1 }, dx[] = { 0, 0, -1, 1, -1, 1, -1, 1 };
int cnt_k, y_post, x_post;
char vil[50][51];
vector<int> hhh;

// low ~ high의 고도사이로 탐색을 했을때, 배달 할 수 있는 집의 개수를 리턴
int bfs(int low, int high) {
	// to-do
	int cnt = 0;
	bool vt[50][50] = { false, };
	queue<pii> q;
	q.push(pii(y_post, x_post));
	vt[y_post][x_post] = true;
	if (h[y_post][x_post] < low || high < h[y_post][x_post]) return -1;
	while (!q.empty() && cnt < cnt_k) {
		pii cur = q.front();
		q.pop();
		for (int i = 0; i < 8; i++) {
			int nxty = cur.first + dy[i], nxtx = cur.second + dx[i];
			if (nxty < 0 || n <= nxty || nxtx < 0 || n <= nxtx) continue;
			if (vt[nxty][nxtx]) continue;
			if (h[nxty][nxtx] < low || high < h[nxty][nxtx]) continue;
			if (vil[nxty][nxtx] == 'K') {
				cnt++;
			}
			vt[nxty][nxtx] = true;
			q.push(pii(nxty, nxtx));
		}
	}

	return cnt;
}

// low ~ high의 고도사이로 탐색을 했을때, 배달 할 수 있는 집의 개수를 리턴

//int dfs(int low, int high) {
//  // to-do
//}

int main() {
	//freopen("res/B2842.in", "r", stdin);
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", vil[i]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (vil[i][j] == 'K') {
				cnt_k++;
			}
			else if (vil[i][j] == 'P') {
				y_post = i, x_post = j;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &h[i][j]);
			hhh.push_back(h[i][j]);
			printf("%d", h[i][j]);
		}
	}
}