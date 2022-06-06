import itertools
def solution(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    able = []
    for i in range(1, len(numbers)+1):
        for n in itertools.permutations(numbers, i):
            num = "".join(n)
            if int(num) not in able and is_prime(int(num)):
                able.append(int(num))

    # def dfs(num):
    #     print(num)
    #     if len(num) == len(numbers) or (len(num) and is_prime(int(num))):
    #         if len(num) and is_prime(int(num)) and int(num) not in answer:
    #             answer.append(int(num))
    #         return
    #
    #     for number in numbers:
    #         dfs(num+number)
    #
    # dfs("")
    return len(able)

print(solution("17"))
print(solution("011"))