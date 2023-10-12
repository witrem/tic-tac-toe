"""win conditions

123
1xxx| ---| --- 
2---| xxx| --- 
3---| ---| xxx 

x--| -x-| --x
x--| -x-| --x
x--| -x-| --x

x--| --x
-x-| -x-
--x| x--
"""
import random

class Board:
    def __init__(self):
        self.table = ['-','-','-','-','-','-','-','-','-',] 
        self.current_winner = None

    def TakeInput(self):
        while True:
            x = input("to play input row column like '2 2','3 3'")
            x = x.split(" ")
            index = (int(x[0])-1)*3 + int(x[1])
            if self.table[index-1] == "-":
                return index
                break
            else:
                print("occupied already")
                continue
        
    def InsertInput(self,input,xo):
        if self.table[input] != "o":
            self.table[input] = xo
        else:
            print("occupied by computer")
           
    def DisplayTable(self):
        print(self.table[0],self.table[1],self.table[2])
        print(self.table[3],self.table[4],self.table[5])
        print(self.table[6],self.table[7],self.table[8])
        
    def is_win(self,i):
        a = ["x","x","x"]
        b = ["o","o","o"]
        
        if i[0:3] == a or i[0:3] == b \
            or i[3:6] == a or i[3:6] == b \
            or i[6:9] == a or i[6:9] == b:
            return True
        if i[0:7:3] == a or i[0:7:3] == b \
            or i[1:8:3] == a or i[1:8:3] == b \
            or i[2:9:3] == a or i[2:9:3] == b:
            return True
        if i[0:9:4] == a or i[0:9:4] == b \
            or i[2:7:2] == a or i[2:7:2] == b:
            return True
            
    
    def TakeInputComputer(self):
        while True:
            a = random.randint(0,8)
            if self.table[a] == "-":
                return a
                break
            else:
                continue
    
    def ResetTable(self):
        self.table = ['-','-','-','-','-','-','-','-','-',] 

play = Board()
play.DisplayTable()
while True:
    p_move = play.TakeInput() -1
    play.InsertInput(p_move,"x")
    play.DisplayTable()   
    print("player played")

    c_move = play.TakeInputComputer()
    play.InsertInput(c_move,"o")
    play.DisplayTable()
    print("computer played")

    if play.is_win(play.table):
        print("player/computer won")
        play.ResetTable()
        play.DisplayTable()
        continue





