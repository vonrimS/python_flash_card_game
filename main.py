from tkinter import *


BG_COLOR = "#B1DDC6"


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
canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
canvas.create_text(400, 270, text="Word", font=('Ariel', 60, 'bold'))

canvas.grid(row=0, column=0, columnspan=3)

wrong = PhotoImage(file="false.png")
nok_button = Button(image=wrong, bg=BG_COLOR, activebackground=BG_COLOR, borderwidth=0)
nok_button.grid(row=1, column=0, sticky='n')

right = PhotoImage(file="true.png")
ok_button = Button(image=right, bg=BG_COLOR, activebackground=BG_COLOR, borderwidth=0)
ok_button.grid(row=1, column=2, sticky='n')

app_window.mainloop()

