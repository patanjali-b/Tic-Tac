import random

def win(A,c1,c2):
    vic = -1
    for mch1 in range(3):
        flag1 = 0
        for ch1 in range(3):                     # Win in First column
            if A[ch1][mch1] == c1:
                flag1 += 1
            else:
                flag1 = 0
        if  flag1 == 3:
                print("Congrats! ", p1, " You win the game")
                return -1

    for mch1 in range(3):
        flag1 = 0
        for ch1 in range(3):                     # Win in First column
            if A[ch1][mch1] == c2:
                flag1 = flag1 + 1
            else:
                flag1 = 0
        if flag1 == 3:
                print("Congrats! ", p2, " You win the game")
                return -1

    for mch1 in range(3):
        flag1 = 0
        for ch1 in range(3):                     # Win in First row
            if A[mch1][ch1] == c1:
                flag1 += 1
            else:
                flag1 = 0
        if flag1 == 3:
            print("Congrats! ", p1, " You win the game")
            return -1

    for mch1 in range(3):
        flag1 = 0
        for ch1 in range(3):                     # Win in First row
            if A[mch1][ch1] == c2:
                flag1 = flag1 + 1
            else:
                flag1 = 0
        if flag1 == 3:
            print("Congrats! ", p2, " You win the game")
            return -1
        
        flag1 = 0
        for ch1 in range(3):                     # Win in Diagonal
            if A[ch1][ch1] == c1:
                flag1 += 1
            else:
                flag1 = 0
        if A[0][0] == c1 and flag1 == 3:
                print("Congrats! ", p1, " You win the game")
                return vic


        flag1 = 0
        for ch1 in range(3):                     # Win in Diagonal
            if A[ch1][ch1] == c2:
                flag1 = flag1 + 1
            else:
                flag1 = 0
        if flag1 == 3:
                print("Congrats! ", p2, " You win the game")
                return vic
    flag1 = 0        
    for mch1 in range(3):     
        for ch1 in range(3):
            if (mch1 + ch1 == 2) and A[mch1][ch1] == c1:
                flag1 = flag1 +1
    if flag1 == 3:
            print("Congrats ", p1, " You win the game")
            return vic
            #####

    flag1 = 0
    for mch1 in range(3):
        for ch1 in range(3):
            if (mch1 + ch1 == 2) and A[mch1][ch1] == c2:
                flag1 = flag1 + 1
    if flag1 == 3:
            print("Congrats ", p2, " You win the game")
            return vic
    return 

D = {}
p1 = input("Enter Player-1's name :- ")
c1 = input("What Do you want as your card? X - O :- ")
p2 = input("Enter Player-2's name :- ")
if c1 == "X":
    print("Hey ", p2, "You get O")
    c2 = "O"
else:
    print("Hey ", p2, "You get X")
    c2 = "X"
D = {c1:p1, c2 : p2}
A = []
print("Let's get started")
for i in range(3):
    row = []
    for j in range(3):
        row.append("_")
    A.append(row)
for i in range(3):
    for j in range(3):
        print(A[i][j],end = " ")
    print("")
print("Let's PLay this Row and Column wise with 1-indexing: ")
print("Example: IF You enter 1 2 as input, the following will be the output: ")
for i in range(3):
    for j in range(3):
        if i == 0 and j == 1:
            print("*", end = " ")
        else:
          print("_",end = " ")
    print("")
flag1 = 0
flag2 = 0 
print("Player 1 starts: Your card is ", c1)
for c in range(9):
   print("Enter co-ordinates ")
   x,y = input().split()
   if c%2 == 0:
       A[int(x)-1][int(y)-1] = c1
   else:
       A[int(x)-1][int(y)-1] = c2
   for i in range(3):
    for j in range(3):
        print(A[i][j],end = " ")
    print("")
   vic = win(A,c1,c2)
   if vic == -1:
       print("Thank you for playing")
       flag2 = 1
       break
if flag2 == 0:
    print("It's a draw, Thanks for Playing")




        
    

        
   



    
    


