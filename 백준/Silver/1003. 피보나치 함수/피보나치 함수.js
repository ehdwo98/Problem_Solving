const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
.map((v) => v.split(" ").map((v) => Number(v)))
//기본세팅 완료

let [T, ...arr] = input
T=T[0]

for(let i=0;i<T;i++){
    let n = arr[i]
    
    let fibo = []//피보나치 배열
    fibo[0] = [1,0]
    fibo[1] = [0,1]
    
    for(let j=2;j<=n;j++){//n번째 피보나치 구하기
        fibo[j]=[fibo[j-1][0]+fibo[j-2][0],fibo[j-1][1]+fibo[j-2][1]]
    }
    
    console.log(fibo[n].join(' '))
}