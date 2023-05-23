from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data=pandas.read_csv("data\wordstolearn.csv")
except FileNotFoundError:
    data=pandas.read_csv("data\Hindi_words.csv")
to_learn=data.to_dict(orient="records")
curr_word={}

def next_card():
    global curr_word,flip_timer
    window.after_cancel(flip_timer)
    curr_word=random.choice(to_learn)   
    canvas.itemconfig(card_title,text="Hindi",fill="black")
    canvas.itemconfig(card_word,text=curr_word["Hindi"],fill="black")
    canvas.itemconfig(canvas_img,image=card_front_img)
    flip_timer=window.after(3000,func=flip_cards) 

def is_known():
    to_learn.remove(curr_word)
    rem_data=pandas.DataFrame(to_learn)
    rem_data.to_csv("data\wordstolearn.csv",index=False)
    next_card()

def flip_cards():
    canvas.itemconfig(canvas_img,image=card_back_img)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=curr_word["English"],fill="white")

window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_cards) 

canvas= Canvas(width=800,height=526)
card_front_img=PhotoImage( file="images\card_front.png")
card_back_img=PhotoImage( file="images\card_back.png")
canvas_img=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,100,text="Title", font=("Ariel",35,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Arial",40,"bold"))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_img=PhotoImage(file="images\wrong.png")
unknown_button=Button(image=wrong_img,highlightthickness=0,command=next_card) 
unknown_button.grid(row=1,column=0)    

check_img=PhotoImage(file=r"images\right.png")
known_button=Button(image=check_img,highlightthickness=0,command=is_known )
known_button.grid(row=1,column=1)

next_card()


window.mainloop()
