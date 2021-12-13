function secToTime(SS){
  let HH = parseInt(SS /3600);
  SS = SS % 3600;
  let MM = parseInt(SS / 60);
  SS = SS % 60;
  HH = HH > 9 ? HH : '0' + HH;
  MM = MM > 9 ? MM : '0' + MM;
  SS = SS > 9 ? SS : '0' + SS;
  return `${HH}:${MM}:${SS}`
}
function timeToSec(time){
  let [hour, min, sec] = time.split(":").map((str)=>parseInt(str));
  return hour*3600 + min * 60 + sec
}
function solution(play_time, adv_time, logs) {
  if (play_time === adv_time){
      return "00:00:00";
  }
  var answer = '';
  let pt = timeToSec(play_time);
  let at = timeToSec(adv_time);
  let time = new Array(pt).fill(0);
  
  for(let log of logs){
      let [start, end] = log.split("-").map(time => timeToSec(time));
      time[start-1] += 1;
      time[end -1] -= 1;
  }
  for(let idx =1; idx < pt; idx++){
     time[idx] += time[idx-1];
  }
  for(let idx = 1; idx < pt; idx++){
      time[idx] += time[idx-1];
  }
   let sum = time[at-1];
let idx = 0;
 for(let i = at-1; i < pt; i++) {
  if(sum < time[i] - time[i-at]) {
    sum = time[i] - time[i-at];
    idx = i - at + 2;
  }
}
  answer = secToTime(idx);
  
  
  return answer;
}