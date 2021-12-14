const card_pos = new Map();
let board = 	[[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]];
// 4x4의 크기이므로 해당 크기만큼 중첩 반복
for(let i = 0; i < 4; i++) {
  for(let j = 0; j < 4; j++) {
    // 해당 좌표의 값이 있다면 카드가 있다는 의미
    if(board[i][j]) {
      // 현재 좌표에서의 카드 캐릭터 번호를 구하고
      const card = board[i][j];
      // 이미 그 카드값을 저장한 적 있다면
      if(card_pos.has(card)) {
        // 카드값의 기존 value(배열)을 구해서
        const origin = card_pos.get(card);
        // 카드값을 갱신
        card_pos.set(card, [...origin, [i, j]]);
      } else {
        // 카드값을 처음 저장하는 경우엔 바로 좌표값 저장
        card_pos.set(card, [ [i, j] ]);
      }
    }
  }
}

const getPermutation = (arr, n) => {
  if(n === 1) return arr.map(el => [el]);
  const result = [];
  
  arr.forEach((fixed, idx, origin) => {
    const rest = [...origin.slice(0, idx), ...origin.slice(idx+1)];
    const perms = getPermutation(rest, n-1);
    const attached = perms.map(perm => [fixed, ...perm]);
    result.push(...attached);
  });
  
  return result;
}
;