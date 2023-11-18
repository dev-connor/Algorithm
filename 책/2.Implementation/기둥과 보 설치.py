def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0: # 기둥
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer: # 바닥 위 or 보의 한쪽 끝부분ㅇ 위 or 다른 기둥 위
                continue
            return False
        elif stuff == 1: # 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer): # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame # stuff 0,1 = 기둥,보 / operate 0,1 = 삭제,설치
        if operate == 0: # 삭제
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate == 1: # 설치
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)

if __name__ == '__main__':
    array = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    result = solution(5,array)
    print(result)

