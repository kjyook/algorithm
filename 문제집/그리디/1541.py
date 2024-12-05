import sys
input = sys.stdin.readline

expression = list(input().rstrip())
answer = []
temp = ''

for i in expression:
    if i == '-' or i == '+':
        if temp == '':
            answer.append(i)
        else:
            answer.append(int(temp))
            temp = ''
            answer.append(i)
    else:
        temp += i

if temp != '':
    answer.append(int(temp))

toggle = True
sum = 0

for i in answer:
    if i == '-':
        toggle = False
        continue

    if i == '+':
        continue
    
    if toggle:
        sum += i
    else:
        sum -= i

print(sum)