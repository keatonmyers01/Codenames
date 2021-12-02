#main file
import random
import requests

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
    word_key = [["fill" for i in range(5)]for j in range(5)]
    counter = 0
    for x in range(5):
        for y in range(5):
            word_key[x][y] = word_set[counter]
            counter = 1 + counter
    return word_key

def gameround(word_key, board_key, used_key, team_color):
    redcounter = 0
    bluecounter = 0
    move_limit = 0
    while(move_limit < 1):
        move_limit = int(input("input number of moves being made: "))+1

    run = True
    for move_count in range(1,move_limit+1):
        print2dArray(word_key)
        if(move_count == move_limit):
            cont = ""
            while(cont != "n" and cont != "y"):
                cont = input("would you like to risk revealing another agent? (y/n): ")
                if(cont == "n"):
                    run = False
        if(run):
            x_loc = -1
            y_loc = -1
            selection = False
            while(not selection):
                while (x_loc not in range(5)):
                    x_loc = int(input("enter x location for selection (1-5): "))-1
                while (y_loc not in range(5)):
                    y_loc = int(input("enter y location for selection (1-5): "))-1
                if(used_key[4-y_loc][x_loc] == False):
                    selection = True
            word_key[4-y_loc][x_loc] = board_key[4-y_loc][x_loc]
            if(board_key[4-y_loc][x_loc] == "black"):
                print("you hit the double agent and lose the game")
                exit()
            elif(board_key[4-y_loc][x_loc] != team_color):
                print("you didn't find your agent better luck next round")
                if team_color=="blue":
                    color="red"
                else:
                    color="blue"
                print2dArray(word_key)
                print("It is now "+color+"'s turn.")
                gameround(word_key, board_key,used_key,color)
            else:
                if team_color=="blue":
                    bluecounter=bluecounter + 1
                    if bluecounter==9:
                        print("Congrats! Blue won this game.")
                        exit()
                else:
                    redcounter=redcounter + 1
                    if redcounter==8:
                        print("Congrats! Red won this game.")
                        exit()
                print("you've revealed your color you have " + str(move_limit-(move_count+1)) + " moves left")
                if move_limit-(move_count+1)==0:
                    if team_color=="blue":
                        color="red"
                    else:
                        color="blue"
                    print2dArray(word_key)
                    print("It is now "+color+"'s turn.")
                    gameround(word_key, board_key,used_key,color)

#Loads the 25 words from an API and retruns it as a list. For api_type 0 is for nouns and 1 is for animals.
def load_api(api_type):
    print("Loading...")
    words = []
    text = "[]"
    for i in range(0, 25):
        if api_type == 0:
            response = requests.get("https://arcane-brushlands-62039.herokuapp.com/api/random")
            text = response.text
        elif api_type == 1:
            response = requests.get("https://random-word-form.herokuapp.com/random/animal")
            text = response.text
        words.append(text[text.index("[")+2:text.index("]")-1])
    print("Loading complete!")
    return words

#Asks user for input on which API they'd like to use.
def ask_api():
    ask = -1
    while ask != 0 and ask != 1:
        ask = int(input("Would you like to play with general nouns (0) or animals (1)? "))
        if(ask != 0 and ask != 1):
            print("Please enter a valid input option!")
    return ask

board_key = make_board_key()
word_key = make_word_key(load_api(ask_api()))
print2dArray(board_key)
print("\n\n")
print2dArray(word_key)
used_key = [[False for i in range(5)] for j in range(5)] #keep this
gameround(word_key, board_key, used_key, "blue")
print2dArray(word_key)
