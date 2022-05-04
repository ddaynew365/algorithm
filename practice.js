function solution(S) {
    // write your code in JavaScript (Node.js 8.9.4)
    let cur = new Set();
    let count = 1
    for (i of S){
        if (cur.has(i)) {
            cur = new Set()
            cur.add(i)
            count += 1
        }
        else cur.add(i)
    }
    console.log(count)
    return count
}


console.log(solution("aaaabbb"))
