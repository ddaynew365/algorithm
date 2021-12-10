let ans = {};
// 조합 구하는 함수
function combinations(array, comb, num){
    if(comb.length === num) {
        comb.sort();
        comb = comb.join("");
        if (comb in ans) ans[comb] += 1;        
        else ans[comb] = 1;
        return;
    }
    array.forEach(element => {
        let next_comb = [...comb, element];
        let next_array = array.filter((_, idx) => idx > array.indexOf(element));
        combinations(next_array, next_comb, num)
    })
}

// main 함수
function solution(orders, course) {
    let answer = [];
    course.forEach(num =>{
        ans ={}
        orders.forEach(order =>{
            combinations(order.split(""), [], num);
        })
        let max = Math.max(...Object.values(ans));
       
        answer = max > 1 ? [
            ...Object.keys(ans).filter(key => ans[key] === max),
            ...answer
            ] : answer
        
    })
    answer.sort()
    return answer;
}

let orders = ["XYZ", "XWY", "WXA"]
let course =[2,3,4];
solution(orders, course);