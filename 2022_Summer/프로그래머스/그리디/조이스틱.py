def solution(name):
    name = list(name)

    alp = ["A", "B", "C", "D", "E",
           "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O",
           "P", "Q", "R", "S", "T",
           "U", "V", "W", "X", "Y", "Z"]

    #cur = list("A" * len(name))
    answer = 0
    nxt = 0
    min_move = len(name) - 1

    for i, char in enumerate(name):
        #print(alp.index(name[i]), list(reversed(alp)).index(name[i]) + 1)
        # 상하 이동
        #answer += min(alp.index(name[i]), list(reversed(alp)).index(name[i]) + 1)
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        # 좌우 이동
        # 경우의 수
        # 1. 한번에 쭉(A안만남) -> 제일 빠름 그냥 계속가면됨
        # 2. A만나면 다시 뒤로 돌아가기
        nxt = i + 1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1

        min_move = min(min_move, i + i + len(name) - nxt, i + 2 * (len(name) - nxt))
    answer += min_move
    return answer
        # 틀린 로직 -> 일부 테케 틀림
        # front = -1
        # back = -1
        # for f in range(i, len(name)+i):
        #     front += 1
        #     f %= len(name)
        #     if cur[f] != name[f]:
        #         break
        #
        # for b in range(i, -len(name), -1):
        #     back += 1
        #     if cur[b] != name[b]:
        #         break
        # #print("name : ", name)
        # #print("cur : ", cur)
        #
        # #print("front: ", front)
        # #print("back: ", back)
        # if abs(front) <= abs(back):
        #     i = (i + front) % len(name)
        #     answer += front
        # else:
        #     i -= back
        #     answer += back
    #return answer

print(solution("JEROEN"))
print(solution("JAN"))