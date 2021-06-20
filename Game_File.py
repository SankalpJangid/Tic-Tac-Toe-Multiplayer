import socket
import threading
import tkinter as tk
from tkinter import *
import sys
import random

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#you can use over another system by just forwarding your tcp port and put new host name and port name
client.connect(("localhost",55555))

nickname = input("choose your name in game : ")

count = 1
board = [" "]*9
player1 = True
number = [0,1,2,3,4,5,6,7,8]

class Game:
    #below single player code
    def printXY(self,x,game_board):
        global number
        number.remove(x)
        if board[x] == "X" or board[x] == "O":
            print("slot already occupied")
            l10 = Label(game_board,text="Slot Occupied")
            l10.grid(row=4,column=2)
        else:
            print(number)
            board[x] = "X"
            l10 = Label(game_board,text="Player O turn")
            l10.grid(row=4,column=2)

            if(len(number) > 1):
                y = random.choice(number)
                print(y)
                board[y] = "O"
                number.remove(y)
                print(number)
                l10 = Label(game_board,text="Player X turn")
                l10.grid(row=4,column=2)
            self.player_board(game_board)

    def single_player_reset(self,game_board):
        global board,number,player1,count
        count = 1
        board.clear()
        board = [" "]*9
        number.clear()
        number = [0,1,2,3,4,5,6,7,8]
        player1 = True
        self.player_board(game_board)

    def player_board(self,game_board):
        global count
        check,name = self.check_result()
        if (check == "won"):
            print(name)
            l10 = Label(game_board,text=f"{name} Player Won")
            l10.grid(row=4,column=2)
            l11 = Button(game_board,text="RESET",command=lambda *args: self.single_player_reset(game_board))
            l11.grid(row=4,column=3)

        if count == 1:
            l10 = Label(game_board,text="Player X turn")
            l10.grid(row=4,column=2)
            count += 1    
        
        l1 = Button(game_board,command=lambda *args: self.printXY(0,game_board), text = f"{board[0]}",width=13,height=5)
        l1.grid(row = 1, column = 1)
        l2 = Button(game_board,command=lambda *args: self.printXY(1,game_board), text = board[1], width=13,height=5)
        l2.grid(row = 1, column = 2 )
        l3 = Button(game_board, command=lambda *args: self.printXY(2,game_board),text = board[2],width=13,height=5)
        l3.grid(row = 1, column = 3)

        l4 = Button(game_board,command=lambda *args: self.printXY(3,game_board), text = board[3],width=13,height=5)
        l4.grid(row = 2, column = 1)
        l5 = Button(game_board,command=lambda *args: self.printXY(4,game_board), text = board[4], width=13,height=5)
        l5.grid(row = 2, column = 2 )
        l6 = Button(game_board,command=lambda *args: self.printXY(5,game_board), text = board[5],width=13,height=5)
        l6.grid(row = 2, column = 3)

        l7 = Button(game_board,command=lambda *args: self.printXY(6,game_board), text = board[6],width=13,height=5)
        l7.grid(row = 3, column = 1)
        l8 = Button(game_board,command=lambda *args: self.printXY(7,game_board), text = board[7], width=13,height=5)
        l8.grid(row = 3, column = 2 )
        l9 = Button(game_board,command=lambda *args: self.printXY(8,game_board), text = board[8],width=13,height=5)
        l9.grid(row = 3, column = 3)

        game_board.mainloop()

    def single_player(self,game_board):
        game_board.destroy()
        game_board = Tk()
        game_board.geometry("300x300")
        game_board.title("Tic Tac Toe")
        self.player_board(game_board)

    #check result function
    def check_result(self):
        if(board[0] == "X" and board[1] == "X" and board[2] =="X"):
            print("X player won")
            return "won","X"  
        if(board[0] == "O" and board[1] == "O" and board[2] =="O"):
            print("O player won")
            return "won","O"
        if(board[3] == "X" and board[4] == "X" and board[5] == "X"):
            print("X player won")
            return "won","X"
        if(board[3] == "O" and board[4] == "O" and board[5] == "O"):
            print("O player won")
            return "won","O"
        if(board[6] == "X" and board[7] == "X" and board[8] == "X"):
            print("X player won")
            return "won","X"
        if(board[6] == "O" and board[7] == "O" and board[8] == "O"):
            print("O player won")
            return "won","O"
        if(board[0] == "X" and board[3] == "X" and board[6] == "X"):
            print("X player won")
            return "won","X"
        if(board[1] == "X" and board[4] == "X" and board[7] == "X"):
            print("X player won")
            return "won","X"
        if(board[2] == "X" and board[5] == "X" and board[8] == "X"):
            print("X player won")
            return "won","X"
        if(board[0] == "O" and board[3] == "O" and board[6] == "O"):
            print("O player won")
            return "won","O"
        if(board[1] == "O" and board[4] == "O" and board[7] == "O"):
            print("O player won")
            return "won","O"
        if(board[2] == "O" and board[5] == "O" and board[8] == "O"):
            print("O player won")
            return "won","O"
        if(board[0] == "X" and board[4] == "X" and board[8] == "X"):
            print("X player won")
            return "won","X"
        if(board[2] == "X" and board[4] == "X" and board[6] == "X"):
            print("X player won")
            return "won","X"
        if(board[0] == "O" and board[4] == "O" and board[8] == "O"):
            print("O player won")
            return "won","O"
        if(board[2] == "O" and board[4] == "O" and board[6] == "O"):
            print("O player won")
            return "won","O"  
        return "not","s"

    #below multiplayer code
    def multi_player(self,game_board):
        game_board.destroy()
        game_board = Tk()
        game_board.geometry("300x300")
        game_board.title("Tic Tac Toe Multi Player")
        label = Label(game_board,text="Enter Room Name",height=5,width=20)
        label.pack(pady=10)
        inputtxt = Text(game_board,
                    height = 1,
                    width = 20)
        inputtxt.pack(pady=20)
        button = Button(game_board,text="Create",command=lambda *args: self.print_input(inputtxt,game_board),width=20,height=1, bg="red",fg="black",relief="raised")
        button.pack(pady=20)
        game_board.mainloop()

    def board(self):
        menu = Tk()
        menu.geometry("300x300")
        menu.title("Tic Tac Toe")
        button1 = tk.Button(menu , text='Single Player VS CPU',command=lambda *args: self.single_player(menu),width=300,bd=10, bg='grey', fg='black', font=('helvetica', 9, 'bold'))
        button2 = tk.Button(menu , text='Player VS Friend',command=lambda *args: self.multi_player(menu),width=300,bd=10, bg='grey', fg='black', font=('helvetica', 9, 'bold'))
        button3 = tk.Button(menu , text='EXIT', bg='grey',command=sys.exit,width=300,bd=10, fg='red', font=('helvetica', 9, 'bold'))
        button1.pack(side="top",pady=20)
        button2.pack(side="top",pady=20)
        button3.pack(side="top",pady=20)
        menu.mainloop()

    def multi_player_board(self,game_board,inp):
        game_board.destroy()
        game_board = Tk()
        game_board.geometry("300x300")
        game_board.title("Tic Tac Toe Multi Player")
        self.multi_board(game_board,inp)

    def resetGame(self,game_board,inp):
        global board,player1,count
        player1 = True
        count = 1
        board.clear()
        board = [" "]*9
        l11 = Button(game_board,text=" ",width=10)
        l11.grid(row=4,column=3)
        self.multi_board(game_board,inp)

    def multi_board(self,game_board,inp):
        global count
        if count == 1:
            threading.Thread(target=self.new_receive, args=(game_board,inp)).start()
            l10 = Label(game_board,text="Player X turn")
            l10.grid(row=4,column=2)
            count += 1

        check,name = self.check_result()
        if (check == "won"):
            print(name)
            l10 = Label(game_board,text=f"{name} Player Won")
            l10.grid(row=4,column=2)
            l11 = Button(game_board,text="RESET",command=lambda *args: self.resetGame(game_board,inp))
            l11.grid(row=4,column=3)

        l1 = Button(game_board,command=lambda *args: self.printXY_multi(0,game_board,inp), text = board[0],width=13,height=5)
        l1.grid(row = 1, column = 1)
        l2 = Button(game_board,command=lambda *args: self.printXY_multi(1,game_board,inp), text = board[1], width=13,height=5)
        l2.grid(row = 1, column = 2 )
        l3 = Button(game_board, command=lambda *args: self.printXY_multi(2,game_board,inp),text = board[2],width=13,height=5)
        l3.grid(row = 1, column = 3)

        l4 = Button(game_board,command=lambda *args: self.printXY_multi(3,game_board,inp), text = board[3],width=13,height=5)
        l4.grid(row = 2, column = 1)
        l5 = Button(game_board,command=lambda *args: self.printXY_multi(4,game_board,inp), text = board[4], width=13,height=5)
        l5.grid(row = 2, column = 2 )
        l6 = Button(game_board,command=lambda *args: self.printXY_multi(5,game_board,inp), text = board[5],width=13,height=5)
        l6.grid(row = 2, column = 3)

        l7 = Button(game_board,command=lambda *args: self.printXY_multi(6,game_board,inp), text = board[6],width=13,height=5)
        l7.grid(row = 3, column = 1)
        l8 = Button(game_board,command=lambda *args: self.printXY_multi(7,game_board,inp), text = board[7], width=13,height=5)
        l8.grid(row = 3, column = 2 )
        l9 = Button(game_board,command=lambda *args: self.printXY_multi(8,game_board,inp), text = board[8],width=13,height=5)
        l9.grid(row = 3, column = 3)

        l10 = Label(game_board,text=f"Room : {inp}")
        l10.grid(row=4,column=1)

        game_board.mainloop()


    def new_receive(self,game_board,inp):
        while True:
            try:
                message = client.recv(1024).decode("ascii")
                print(message[-1])
                self.printValueOnBoard(message,game_board,inp)               
            except Exception as e:
                print(e)

    def printXY_multi(self,x,game_board,inp):
        client.send(f"number {str(inp)} {str(x)}".encode("ascii"))
        threading.Thread(target=self.new_receive, args=(game_board,inp)).start()

    def printValueOnBoard(self,message,game_board,inp):
        global player1
        ms= int(float(message[-1]))
        if board[ms] == "X" or board[ms] == "O":
            print("slot already occupied")
        else:
            if player1 == True:
                if board[ms] == "X" or board[ms] == "O":
                    print("slot already occupied")
                    l10 = Label(game_board,text="Slot Occupied")
                    l10.grid(row=4,column=2)
                else:
                    board[ms] = "X"
                    l10 = Label(game_board,text="Player O turn")
                    l10.grid(row=4,column=2)
                    player1 = False
                    self.multi_board(game_board,inp)
            else:
                if board[ms] == "X" or board[ms] == "O":
                    print("slot already occupied")
                    l10 = Label(game_board,text="Slot Occupied")
                    l10.grid(row=4,column=2)
                else:
                    board[ms] = "O"
                    l10 = Label(game_board,text="Player X turn")
                    l10.grid(row=4,column=2)
                    player1 = True
                    self.multi_board(game_board,inp)

    def print_input(self,inputtxt,game_board):
        inp = inputtxt.get(1.0,"end-1c")
        client.send(f"room {str(inp)}".encode("ascii"))
        self.multi_player_board(game_board,inp)

def receive():
    while True:
        try:
            obj = Game()
            message = client.recv(1024).decode("ascii")
            if(message == "NICK"):
                client.send(nickname.encode("ascii"))
                obj.board()
            
        except:
            print("not working")
            client.close()
            break

t1 = threading.Thread(target=receive)
t1.start()
