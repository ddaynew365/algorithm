function makePw(n, fares) {
  let graph = Array.from({length: n}, (_, i) => Array.from({length: n}, (_, j)=> i === j ? 0 : Infinity));
  fares.forEach((list) => {
      let [i, j, v] = list;
      graph[i-1][j-1] = v;
      graph[j-1][i-1] = v;
  })
  
  for(let num = 0; num < n; num++){
      for (let i = 0; i < n; i++){
          for (let j = 0; j < n; j++){
              if(graph[i][j] > graph[i][num] + graph[num][j]) graph[i][j] = graph[i][num] + graph[num][j]
          }
      }
  }
  return graph;
}

function solution(n, s, a, b, fares) {
  [s, a, b] = [s-1, a-1, b-1];
  let answer = Infinity;
  const table = makePw(n, fares);
  for(let i = 0; i < n; i++){
     if (answer > (table[s][i] + table[i][a] + table[i][b])){
         answer = table[s][i] + table[i][a] + table[i][b];
     }
  }
  return answer;
}

console.log(solution(
  6,	4,	6,	2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
	