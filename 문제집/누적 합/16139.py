import sys
import string
import copy
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

question = []
for _ in range(q):
    a, b, c = input().split()
    question.append([str(a), int(b), int(c)])
word = {char: idx for idx, char in enumerate(string.ascii_lowercase)}

#그냥 다 check한다면 q * (문자열의 길이) 만큼 걸릴 것이다.
#2차원 리스트를 이용해서 구해보자. 알파벳은 0부터 순서대로 a이다. dp x,y 는 x + 1번째 문자열까지에서 y번째 알파벳의 갯수이다.
#시간 복잡도는 dp구하는데 len(s) 답 내는데 q 걸린다. 상수의 시간대로 시간복잡도를 줄일 수 있다.
dp = [[0] * 26 for _ in range(len(s) + 1)]

for idx, char in enumerate(s):
    if idx == 0:
        dp[idx][word[char]] = 1
        continue

    # 깊은 복사와 얕은 복사
    #dp[idx] = copy.deepcopy(dp[idx - 1])는 깊은 복사로 dp[idx]와 dp[idx - 1]은 같은 객체를 참고하지 않고 값만 빌려온다
    #dp[idx] = dp[idx - 1] 는 얕은 복사로 둘은 같은 객체를 참고하게 되어 같이 값이 변한다. 이는 옳지 않다
    #copy.deepcopy는 물론 좋지만 O(26)의 시간복잡도를 가진다. 귀찮아지니 slicing을 이용해서 새list를 만드는 아래의 방법도있다.
    #이거 바꾸니가 50점에서 100점이 되었다.
    dp[idx] = dp[idx - 1][:]
    dp[idx][word[char]] += 1

def answer(a):
    if a[1] == 0:
        print(dp[a[2]][word[a[0]]])
    else:
        print(dp[a[2]][word[a[0]]] - dp[a[1] - 1][word[a[0]]])
    return

for q in question:
    answer(q)