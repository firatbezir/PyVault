from tkinter import *

# -------------------------- CONSTANTS --------------------------
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
# ------------------------------ UI ------------------------------

window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img_front)
canvas.create_text(400, 150, text="French", fill="black", font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 263, text="...", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(columnspan=2, column=0, row=0)

# Buttons
img_wrong = PhotoImage(file="images/wrong.png")
img_right = PhotoImage(file="images/right.png")

btn_wrong = Button(image=img_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0)
btn_wrong.grid(column=0, row=1)

btn_right = Button(image=img_right, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0)
btn_right.grid(column=1, row=1)


window.mainloop()
