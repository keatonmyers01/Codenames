#main file
import random

#makes and returns a 2d array containing a string of "blue", "red", "white", or "black"
def make_board_key():
    keyArr = [["white" for x in range(5)] for y in range(5)]
    for x in range(9):
        while True:
            h = random.randint(0,4)
            w = random.randint(0,4)
            if(keyArr[h][w] == "white"):
                keyArr[h][w] = "blue"
                break
    for y in range(8):
        while True:
            h = random.randint(0,4)
            w = random.randint(0,4)
            if(keyArr[h][w] == "white"):
                keyArr[h][w] = "red"
                break
    while True:
        h = random.randint(0,4)
        w = random.randint(0,4)
        if(keyArr[h][w] == "white"):
            keyArr[h][w] = "black"
            break


    return keyArr
##prints a 5x5 2d array as human readable for debugging
def print2dArray(arr):
    for x in range(5):
        for y in range(5):
            print(arr[x][y] + " ", end="")
        print(" ")

def make_word_key(word_set):
    word_key = [[]]
    counter = 0
    for x in range(5):
        for y in range(5):
            word_key[x][y] = word_set[counter]
            counter = 1 + counter

def gameround(word_key, board_key, used_key, team_color):
    print2dArray(board_key)
    move_limit = 0
    while(move_limit < 1):
        move_limit = input("input number of moves being made: ")+1

    run = True
    for move_count in range(1,move_limit+1):
        if(move_count == move_limit):
            cont = ""
            while(cont != "n" and cont != "y"):
                cont = input("would you like to risk revelaing another agent? (y/n)")
                if(cont == "n"):
                    run = False
        if(run):
            x_loc = 0
            y_loc = 0
            selection = False
            while(selection == False):
                while (x_loc not in range(5)):
                    x_loc = input("enter x location for selection (1-5): ")-1
                while (x_loc not in range(5)):
                    y_loc = input("enter y location for selection (1-5): ")-1
                if(used_key[x_loc][4-y_loc] == False):
                    selection = True
            word_key[x_loc][4-y_loc] = board_key[x_loc][4-y_loc]
            if(board_key[x_loc][4-y_loc] == "black"):
                print("you hit the double agent and lose the game")
                exit()
            elif(board_key != team_color):
                print("you didn't find your agent better luck next round")
                move_count = move_limit
            else:
                print("you've revealed your color you have " + str(move_count - move_limit) + "moves left")



board_key = make_board_key()
word_key = make_word_key()
used_key = [[False for i in range(5)] for j in range(5)] #keep this
print2dArray(board_key)
print2dArray(word_key)
print2dArray(used_key)