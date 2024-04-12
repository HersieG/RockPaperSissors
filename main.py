import random
from tkinter import *





def whoWon(playerChoice):
    choices = ["rock", "paper", "scissors"]


    compChoice = random.choice(choices)

    if compChoice == playerChoice:
        a = "Computer: " + compChoice + "\nYou: " + playerChoice + "\nIt was a tie!"
        screen_Label.set(a)
    if playerChoice == "rock":
        if compChoice == "scissors":
            a = "Computer: " + compChoice + "\nYou: " + playerChoice + "\nYou won!"
            screen_Label.set(a)
        elif compChoice == "paper":
            a = "Computer: " + compChoice + "\nYou: " + playerChoice + "\nYou lost."
            screen_Label.set(a)
    if playerChoice == "scissors":
        if compChoice == "paper":
            a = "Computer: " + compChoice + "\nYou: " + playerChoice + "\nYou won!"
            screen_Label.set(a)

        elif compChoice == "rock":
            a = "Computer: " + compChoice + "\nYou: " + playerChoice + "\nYou lost."
            screen_Label.set(a)
    if playerChoice == "paper":
        if compChoice == "rock":
            a = "Computer: " + compChoice + "\nYou: " + playerChoice + "\nYou won!"
            screen_Label.set(a)
        elif compChoice == "scissors":
            a = "Computer: " + compChoice + "\nYou: " + playerChoice + "\nYou lost."
            screen_Label.set(a)




window = Tk()
window.resizable(height=False, width=False)
screen_text = ""
screen_Label = StringVar()
screen_Label.set("Pick your move!")
label = Label(window,textvariable = screen_Label, font=('consolas', 20), bg="white", width=45, height=4)
label.pack(side="top")

frame = Frame(window)
frame.pack()

window.title("Rock Paper Scissors game")
window.geometry("750x500")

button_Rock = Button(frame,
                         text = "Rock",
                         height = 2,
                         width= 9,
                         command = lambda: whoWon("rock"),
                         font =("Comic Sans",30))
button_Rock.grid(row=2, column=0)

button_Paper = Button(frame,
                         text="Paper",
                         height=2,
                         width=9,
                         command= lambda: whoWon("paper"),
                         font=("Comic Sans", 30))
button_Paper.grid(row=2, column=1)

button_Scissors = Button(frame,
                         text="Scissors",
                         height=2,
                         width=9,
                         command=lambda: whoWon("scissors"),
                         font=("Comic Sans", 30),
                            relief = RAISED,
                             )
button_Scissors.grid(row=2, column=2)

window.mainloop()












