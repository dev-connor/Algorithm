import heapq

# +4
# 현재시간을 t (time) 작업이 요청되는 시점을 s (start),작업의 소요시간을 r (run time) 이라고 하면
# 첫번째작업이 먼저들어간다면 평균시간은 (t + r1 - s1 + t + r1 + r2 - s2) / t = (2t + 2r1 + r2 - s1 - s2) / t
# 두번째작업이 먼저들어간다면 평균시간은 (t + r2 - s2 + t + r2 + r1 - s1) / t = (2t + 2r2 + r1 - s1 - s2) / t
# 평균시간은 r 에 비례하므로, r 을 기준으로 최소힙에 담아 문제를 푼다.
def solution(jobs):
    time = 0
    doing = 0
    jobs.sort()
    h = []
    idx = 0
    done = 0

    while done != len(jobs):

        # 현재 시작할 수 있는 작업 확인
        for j in jobs[idx:]:
            if j[0] <= time:
                heapq.heappush(h, (j[1], j[0]))
                idx += 1 # 다음 작업
            else:
                break

        # 작업 시작
        if len(h) > 0:
            r_time, s_time = heapq.heappop(h)
            time += r_time
            doing += time - s_time
            done += 1
        else: # 현재 작업할 수 있는게 없다면 1초 증가
            time += 1
    return doing // len(jobs)

if __name__ == '__main__':
    array = [[0, 3], [1, 9], [15, 6]]
    result = solution(array)
    print(result)
