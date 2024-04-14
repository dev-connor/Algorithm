import { log } from 'console'
import * as fs from 'fs'

const input = fs.readFileSync('dev/stdin').toString().trim().split(' ')
let [a,b] = input.map((i) => +i)
log(a-b)
