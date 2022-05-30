##
def solution(progresses, speeds):
    day = 1
    cnt = 0
    answer = []
    while progresses:
        if progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        else:
            if cnt:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)
    return answer