from tkinter import *
import random


def play():
    def enter():
        if int(entry.get()) > x and (int(entry.get()) - x) > 15:
            label5 = Label(window1, text="Too high!, guess again",
                           font=("Pacifico", 30, "italic"),
                           fg="#c6cf19", bg="#3285a8")
            label5.pack()

        elif int(entry.get()) > x and (int(entry.get()) - x) < 15:
            label6 = Label(window1, text="High!, guess again",
                           font=("Pacifico", 30, "italic"),
                           fg="#c6cf19", bg="#3285a8")
            label6.pack()

        elif int(entry.get()) < x and (x - int(entry.get())) > 15:
            label7 = Label(window1, text="Too low!, guess again",
                           font=("Pacifico", 30, "italic"),
                           fg="#c6cf19", bg="#3285a8")
            label7.pack()

        elif int(entry.get()) < x and (x - int(entry.get())) < 15:
            label8 = Label(window1, text="low!, guess again",
                           font=("Pacifico", 30, "italic"),
                           fg="#c6cf19", bg="#3285a8")
            label8.pack()

        elif int(entry.get()) == x:
            label9 = Label(window1, text="That is right, Amazing\nYou won...",
                           font=("Pacifico", 30, "italic"),
                           fg="White", bg="#3285a8")
            label9.pack()

    window1 = Tk()
    window1.geometry("1250x680")
    window1.title("Incredible games")
    window1.config(bg="#3285a8")
    label4 = Label(window1, text="I guessed the number,find out what the number is \nLet's guess!",
                   font=("Pacifico", 30, "italic"),
                   fg="#c6cf19", bg="#3285a8")
    x = random.randint(1, 100)
    entry = Entry(window1, font=("Arial", 20), bg="White", fg="Black")
    button1 = Button(window1, text="ENTER", font=("Pacifico", 15, "bold"), relief=RAISED, bd=10, command=enter)

    window.destroy()
    label4.pack()
    entry.pack()
    button1.pack()


window = Tk()

window.geometry("1250x680")
window.title("Incredible games")
window.config(bg="#3285a8")
label1 = Label(window, text="Number Guessing Game", font=("Pacifico", 50, "bold", "italic"),
               fg="White", bg="#3285a8")
label2 = Label(window, text="In this game, I guess a number between 1 and 100 and",
               font=("Pacifico", 30, "italic"),
               fg="#c6cf19", bg="#3285a8")
label3 = Label(window,
               text="you have to find that number, I will give you some amazing hints to guess,\nif you guessed it YOU WON otherwise LOSE!",
               font=("Pacifico", 30, "italic"),
               fg="#c6cf19", bg="#3285a8")
button = Button(window, text="PLAY", font=("Pacifico", 30, "bold"), relief=RAISED, bd=20, command=play)
label1.pack()
label2.pack()
label3.pack()
button.pack()
window.mainloop()
