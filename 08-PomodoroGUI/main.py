import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = 1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 30
    long_break_sec = LONG_BREAK_MIN * 20

    if reps == 8:
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50))
        count_down(long_break_sec)
    elif reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
        count_down(work_sec)
    else:
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            repeat_count = int(reps / 2)
            check_label.config(text="✓" * repeat_count, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25,
                                                                              "bold"))


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Pomodoro Figure
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label
timer_label = Label()
label_fg = GREEN
timer_label.config(text="Timer", fg=label_fg, bg = YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# Start button
start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Restart button
restart_button = Button()
restart_button.config(text="Reset", highlightthickness=0, command=reset_timer)
restart_button.grid(column=2, row=2)

# Check Marks
check_label = Label()
check_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()



