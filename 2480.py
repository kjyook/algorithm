def main():
    n1, n2, n3 = input().split()
    a = int(n1)
    b = int(n2)
    c = int(n3)

    if a== b ==c:
        print(10000 +a*1000)
    elif a == b:
        print(1000 + a*100)
    elif a == c:
        print(1000 + a*100)
    elif b == c:
        print(1000 + b*100)
    else:
        print(max(a,b,c)*100)

if __name__ == "__main__":
    main()