def solution(priorities, location):
    q = []
    for i, p in enumerate(priorities):
        q.append((p, i))

    i = 0
    while q:
        # print(q)
        mq = max(q)
        cur = q.pop(0)
        # print("mq : ", mq)
        if cur[0] == mq[0]:
            i += 1
            if cur[1] == location:
                return i
        else:
            q.append(cur)