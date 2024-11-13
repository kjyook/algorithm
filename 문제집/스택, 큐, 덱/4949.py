import sys

def append_to_stack(stk, a):
    if len(stk) == 0:
        if a == '(' or a == '[':
            stk.append(a)
            return stk
        else:
            return False
    else:
        if a == ')':
            if stk[-1] == '(':
                stk.pop()
                return stk
            else:
                return False
        elif a == ']':
            if stk[-1] == '[':
                stk.pop()
                return stk
            else:
                return False
        else:
            stk.append(a)
            return stk

def main():
    while True:
        string = sys.stdin.readline().rstrip('\n')
        stack = []
        toggle = True

        if string == '.' and len(string) == 1:
            return

        for i in string:
            if i == '[' or i == ']' or i == '(' or i == ')':
                stack = append_to_stack(stack, i)

                if stack == False:
                    print("no")
                    toggle = False
                    break
        
        if toggle and len(stack) ==0:
            print("yes")
        elif toggle and len(stack) != 0:
            print("no")

if __name__ == "__main__":
    main()