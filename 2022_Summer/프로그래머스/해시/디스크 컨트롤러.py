def solution(jobs):
    answer = 0
    t = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬
    print(jobs)
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= t:
                t += jobs[i][1]
                answer += t - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                t += 1

    return answer // length

print(solution([[0, 3], [1, 9], [2, 6]]))