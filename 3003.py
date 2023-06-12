def main():
    
    king, queen, look, bis, knight, pawn = input().split()
    print(1 - int(king), 1 - int(queen),2 - int(look),2 - int(bis),2 - int(knight), 8 - int(pawn))

if __name__ == "__main__":
    main()