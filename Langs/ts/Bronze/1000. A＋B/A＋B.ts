import { log } from 'console'
import * as fs from 'fs'

const input = fs.readFileSync('dev/stdin').toString().trim().split(' ')

//입력 정제하기
let [a, b] = input
log(+a + +b)