const fs = require("fs");
const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
//기본세팅 완료

const [n, ...test] = input//예제 개수, 예제

for (let i = 0; i < n; i++) {
  let info = test[2*i].split(' ').map(Number);
  let arr = test[2*i+1].split(' ').map(Number);//N개의 문서의 중요도 배열

  let N = info[0]//문서의 개수
  let M = info[1]//궁금한 문서 위치(인덱스)
  
  //console.log(N, M, arr);
  
  solution(N,M,arr);
}

function solution(N,M,arr) {
  /**
   * 문제 풀이
   */
  let pivot = M//궁금한 문서의 인덱스
  let cnt = 1
  
  while(arr.length){
      let tmp = arr.shift()//맨 앞의 문서 꺼내기
      let found = arr.find(e => e > tmp)
      
      if(found != undefined){//뒤에 중요도 큰 문서 존재
          arr.push(tmp)//맨 뒤로 보내기
          if(pivot==0){//궁금한 문서
              pivot = arr.length-1//궁금한 문서 위치 조정
          }
          else{//궁금하지 않은 문서
              pivot--//궁금한 문서 위치 조정
              
          }
      }
      else{//인쇄
          if(pivot==0){//궁금한 문서
              console.log(cnt);
              break
          }
          else{//궁금하지 않는 문서
              cnt++//순서 카운트
              pivot--//궁금한 문서 위치 조정
          }
      }
  }  
}