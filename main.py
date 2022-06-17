from tkinter import *
import pandas
import random


BG_COLOR = "#B1DDC6"

data = pandas.read_csv('data/top5000.csv')
to_learn = data.to_dict(orient="records")
# print(to_learn)

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    # print(current_card["French"])


# ----- GUI SETUP -----
app_window = Tk()
app_window.title("Flashy")
app_window.resizable(False, False)
app_window.config(width=1000, height=800, padx=20, pady=20, bg=BG_COLOR)
# Place app window at the center
app_window.eval('tk::PlaceWindow %s center' % app_window.winfo_pathname(app_window.winfo_id()))

canvas = Canvas(width=800, height=500, bg=BG_COLOR, highlightthickness=0)
card_img = PhotoImage(file="card.png")
canvas.create_image(408, 250, image=card_img)
card_title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 270, text="", font=('Ariel', 60, 'bold'))

canvas.grid(row=0, column=0, columnspan=3)

wrong = PhotoImage(file="false.png")
nok_button = Button(image=wrong, bg=BG_COLOR, activebackground=BG_COLOR, borderwidth=0, command=next_card)
nok_button.grid(row=1, column=0, sticky='n')

right = PhotoImage(file="true.png")
ok_button = Button(image=right, bg=BG_COLOR, activebackground=BG_COLOR, borderwidth=0, command=next_card)
ok_button.grid(row=1, column=2, sticky='n')

next_card()

app_window.mainloop()

