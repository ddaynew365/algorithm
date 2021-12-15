function bisect(target, data){
  if (data.length === 0) return 0
  let left = 0;
  let mid = 0;
  let right = data.length;
  while (left < right){
      mid = Math.floor((left + right) / 2);
      if(data[mid] >= target) right = mid;
      else left = mid + 1;
  }
  return data.length - left;
}
function combination(arr, selNum){
  const result = [];
  if (selNum === 1) return arr;
  arr.forEach((fixed, idx, origin) => {
      const rest = origin.slice(idx + 1);
      const comb = combination(rest, selNum - 1);
      const attach = comb.map(el => fixed + el);
      result.push(...attach);
  })
  return result;
}

function solution(info, query) {
  let answer = [];
  let result = {};
  result["all"] = [];
  for (let i of info){
      let comb = [];
      let list = i.split(" ");
      let [cmd, score] = [list.slice(0,-1), parseInt(list[4])];
      result["all"].push(score);
      for (let i = 1; i< 5; i++){
          comb = [...comb, ...combination(cmd, i)];
      }
     for (let c of comb){
         if(c in result) result[c].push(score);
         else result[c] = [score]
         
     }
  }
  for (let q of query){
      let list = q.split(" and ");
      let last =list[3];
      let [lastCmd, score] = last.split(" ");
      list[3] = lastCmd;
      let cmd = list.join("").replace(/\-+/g,"");
      if(cmd === "") cmd = "all";
      if(cmd in result){
          let list = result[cmd].sort((a,b)=> a-b);
          let count = bisect(score, list);
          answer.push(count);
      }
  }
  return answer;
}