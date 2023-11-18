def solution(arr):
    INF = 10 ** 9
    oper_cnt = len(arr) // 2 + 1
    max_dp = [[-INF] * oper_cnt for _ in range(oper_cnt)]
    min_dp = [[INF] * oper_cnt for _ in range(oper_cnt)]

    for i in range(0, oper_cnt):
        max_dp[i][i] = int(arr[2 * i])
        min_dp[i][i] = int(arr[2 * i])

    for cnt in range(1, oper_cnt):
        for i in range(0, oper_cnt - cnt):
            j = i + cnt
            for k in range(i, j):
                if arr[k * 2 + 1] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])

    return max_dp[0][oper_cnt - 1]

if __name__ == '__main__':
    arr = ["1", "-", "3", "+", "5", "-", "8"]
    result = solution(arr)
    print(result)

# 원본 C++ 코드
'''
function solution (arr) {
  const operandsCount = Math.ceil(arr.length / 2);
  const max_dp = new Array(operandsCount).fill().map(_ => new Array(operandsCount).fill(-Infinity));
  const min_dp = new Array(operandsCount).fill().map(_ => new Array(operandsCount).fill(Infinity));
  
  for(let i = 0; i < operandsCount; i++) {
    max_dp[i][i] = +arr[i*2];
    min_dp[i][i] = +arr[i*2];
  }
  
  for(let cnt = 1; cnt < operandsCount; cnt++) {
    for(let i = 0; i < operandsCount - cnt; i++) {
      const j = i + cnt;
      for(let k = i; k < j; k++) {
        if (arr[k*2+1] === '+') {
          max_dp[i][j] = Math.max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j]);
          min_dp[i][j] = Math.min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j]);
        } else {
          max_dp[i][j] = Math.max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j]);
          min_dp[i][j] = Math.min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j]);
        }
      }
    }
  }
  
  return max_dp[0][operandsCount-1];
}
'''