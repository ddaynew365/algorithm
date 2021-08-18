function solution(array, commands) {
    var answer = [];
    for (let command of commands){
        const [j,k,l] = command;
        const slice = array.slice(j-1, k).sort((a,b)=>a-b);
        answer.push(slice[l-1]);
    }
    return answer;
}