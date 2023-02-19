from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
# Colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Font
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 2 == 0:
        if reps % 8 == 0:
            title_label.config(text="Break", fg=RED)
            count_down(LONG_BREAK_MIN * 60)
            return
        else:
            title_label.config(text="Break", fg=PINK)
            count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)  # minutes
    count_sec = count % 60  # seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # add a checkmark after every successful work session
        if reps % 2 == 0:
            checks = "✔" * math.floor(reps / 2)
            check_marks.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
# window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Setting canvas to view tomato image
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# Title label
title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, pady=5)
title_label.grid(row=0, column=1)

# buttons
start_button = Button(text="Start", width=5, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", width=5, highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

# check marks label
check_marks = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
check_marks.grid(row=3, column=1)


window.mainloop()
