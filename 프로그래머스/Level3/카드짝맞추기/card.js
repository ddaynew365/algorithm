function solution(board, r, c) {
  const SIZE = 4; // board의 크기 (1번 조건)
  const moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]; // 북동남서 이동 좌표
  const coordinates = {}; // 카드 번호가 key -> 카드 좌표가 value
  let cards = new Set(); // 카드 목록

  // 게임판을 돌면서 카드 좌표와 카드 목록들을 저장
  board.forEach((row, i) => row.forEach((cell, j) => {
      if (cell) {
          cards.add(cell);
          coordinates[cell] = coordinates[cell] || [];
          coordinates[cell].push([i, j]);
      }
  }));
  cards = [...cards];

  // 카드를 뒤집을 순서를 저장
  const [check, cards_permutation] = [...Array(cards.length)].reduce(m => {
      m[0].push(0);
      m[1].push(0);

      return m;
  }, [[], []]);

  // 게임판 범위내 여부
  const is_range = (y, x) => (0 <= y && y < SIZE && 0 <= x && x < SIZE);

  // 카드와 카드 사이의 최단 거리를 리턴 (3번 계획)
  const get_min_distance = (y1, x1, y2, x2) => {
      const is_arrival = (y, x) => (y == y2 && x == x2);

      // 이미 도착했을 때
      if (is_arrival(y1, x1)) return 0;

      // bfs를 통해서 최단 거리를 구함
      const q = [];
      const visit = [...Array(SIZE)].map(() => [...Array(SIZE)].map(() => 0));
      let ret = 0;

      q.push([y1, x1, 0]);
      visit[y1][x1] = 1;

      a: while (q.length) {
          const [y, x, move_count] = q.shift();

          for (const [my, mx] of moves) {
              // 화살표 이동 (한 칸)
              const ny = y + my;
              const nx = x + mx;

              // 도착하면 while문 break
              if (is_arrival(ny, nx)) {
                  ret = move_count + 1;
                  break a;
              }

              if (is_range(ny, nx) && !visit[ny][nx]) {
                  visit[ny][nx] = 1;
                  q.push([ny, nx, move_count + 1]);
              }

              // Ctrl 이동 (끝 칸)
              let ctrl_y = y;
              let ctrl_x = x;
              while (1) {
                  const tmp_y = ctrl_y + my;
                  const tmp_x = ctrl_x + mx;

                  // 범위 밖일 때
                  if (!is_range(tmp_y, tmp_x)) break;

                  ctrl_y = tmp_y;
                  ctrl_x = tmp_x;

                  // 카드를 만났을 때
                  if (board[ctrl_y][ctrl_x]) break;
              }

              // 도착하면 while문 break
              if (is_arrival(ctrl_y, ctrl_x)) {
                  ret = move_count + 1;
                  break a;
              }

              // 이미 방문했다면
              if (visit[ctrl_y][ctrl_x]) continue;
              
              visit[ctrl_y][ctrl_x] = 1;
              q.push([ctrl_y, ctrl_x, move_count + 1]);
          }
      }

      return ret;
  };

  // 백트래킹으로 카드 순서대로 뒤집어보면서 최소값 리턴 (2번 계획)
  const simulation = (y, x, cost, depth) => {
      // 기저 사례 -> 모든 카드를 뒤집었다면 비용 리턴
      if (depth == cards.length) return cost;

      // 카드
      const card = cards_permutation[depth]; 

      // 카드 좌표
      const [[ay1, ax1], [ay2, ax2]] = coordinates[card]; 

      // 현재 좌표에서 '다음 1번 카드'로 가는 비용 + '다음 1번 카드'에서 '다음 2번 카드'로 가는 비용
      const move_cost1 = get_min_distance(y, x, ay1, ax1) + get_min_distance(ay1, ax1, ay2, ax2); 

      // 현재 좌표에서 '다음 2번 카드'로 가는 비용 + '다음 2번 카드'에서 '다음 1번 카드'로 가는 비용
      const move_cost2 = get_min_distance(y, x, ay2, ax2) + get_min_distance(ay2, ax2, ay1, ax1); 

      // 뒤집음 표시
      board[ay1][ax1] = board[ay2][ax2] = 0; 

      // '다음 2번 카드'에서 그 다음 카드를 뒤집을 비용 vs '다음 1번 카드'에서 그 다음 카드를 뒤집을 비용
      // cost에 +2의 뜻은 다음 카드를 두 번 뒤집었으니 두 번의 enter연산 2를 더해줌 (3번 조건)
      const ret = Math.min(simulation(ay2, ax2, cost + move_cost1 + 2, depth + 1), simulation(ay1, ax1, cost + move_cost2 + 2, depth + 1));

      // 원래 카드 번호로 복구
      board[ay1][ax1] = board[ay2][ax2] = card; 

      return ret;
  };

  // 백트래킹을 통해 카드 순서 생성 (1번 계획)
  return (function f(depth) {
      // 기저 사례 -> 카드 순서를 생성했다면 시뮬레이션 진행
      if (depth == cards.length) return simulation(r, c, 0, 0);

      let ret = 987654321;

      for (let i = 0; i < cards.length; i++) {
          if (check[i]) continue;

          check[i] = 1;
          cards_permutation[depth] = cards[i];
          ret = Math.min(ret, f(depth + 1));
          check[i] = 0;
      }

      return ret;
  })(0)}


  solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0);