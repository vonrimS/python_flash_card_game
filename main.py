import time
from tkinter import *
import pandas
import random



BG_COLOR = "#B1DDC6"
TIMER = 5000

current_card = {}
data = pandas.read_csv('data/top5000.csv')
to_learn = data.to_dict(orient="records")

# Get next random card
def next_card():
    global current_card
    global flip_timer
    app_window.after_cancel(flip_timer)
    canvas.itemconfig(1, state="normal")
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = app_window.after(TIMER, func=revert_card_time_out)

# Flip card with left mouse click on card
def revert_card(event):
    global current_card
    global flip_timer
    app_window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)
    flip_timer = app_window.after(TIMER, func=revert_card_time_out)

# Flip card with time out
def revert_card_time_out():
    global current_card
    global flip_timer
    app_window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)
    flip_timer = app_window.after(TIMER, func=revert_card_time_out)

# ----- GUI SETUP -----
app_window = Tk()
app_window.title("Flashy")
app_window.resizable(False, False)
app_window.config(width=1000, height=800, padx=20, pady=20, bg=BG_COLOR)
# Place app window at the center
app_window.eval('tk::PlaceWindow %s center' % app_window.winfo_pathname(app_window.winfo_id()))

flip_timer = app_window.after(TIMER, func=revert_card_time_out)

# Card face side
canvas = Canvas(width=800, height=500, bg=BG_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="card.png")
card_back_img = PhotoImage(file="card_revert.png")
card_background = canvas.create_image(408, 250, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 270, text="", font=('Ariel', 60, 'bold'))
canvas.bind("<Button-1>", revert_card)
canvas.grid(row=0, column=0, columnspan=3)


wrong = PhotoImage(file="false.png")
nok_button = Button(image=wrong, bg=BG_COLOR, activebackground=BG_COLOR, borderwidth=0, command=next_card)
nok_button.grid(row=1, column=0, sticky='n')

right = PhotoImage(file="true.png")
ok_button = Button(image=right, bg=BG_COLOR, activebackground=BG_COLOR, borderwidth=0, command=next_card)
ok_button.grid(row=1, column=2, sticky='n')

next_card()

app_window.mainloop()
