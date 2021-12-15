function bisect(target, data){
  console.log(target, data);
  if (data.length === 0) return 0
  let left = 0;
  let mid = 0;
  let right = data.length;
  while (left <= right){
      mid = parseInt((left + right) / 2);
      if (data[mid] === target) break;
      else if(data[mid] > target) right = mid;
      else left = mid + 1;
  }
  return data.slice(mid).length;
}
console.log(bisect(200, [150, 210]));