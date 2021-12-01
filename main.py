#main file
import random

#makes and returns a 2d array containing a string of "blue", "red", "white", or "black"
def make_key():
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
