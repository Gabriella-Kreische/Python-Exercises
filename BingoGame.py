#User will choose a random number between 1 and 80
#Number will be match or not with the bingo card
#When all numbers of the bingo card are matched then a BINGO message is delivered and the game is ended
Bingo_Card = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
running = True
sum = 0
print("Welcome to your Bingo Game!")
while running:
    for i in Bingo_Card:
        BN = int(input("Please enter a random number between 1 and 80: "))
        if (BN in Bingo_Card):
            print("Congratulations! This number matched a number in your Bingo Card!")
            Bingo_Card.remove(BN)
            sum = sum + 1
            if sum > 9:
                print("BINGO! All numbers have been matched!")
                running = False
            else:
                print("Your remaining numbers are: "+str(Bingo_Card))
                running = True
        else:
            print("This number is an incorrect guess.")
            running = True