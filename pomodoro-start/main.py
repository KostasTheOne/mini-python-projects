from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0
    check_mark.config(text="", bg=YELLOW, fg=GREEN, font=("Arial", 21))
    timer_label.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8==0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", font = (FONT_NAME, 32, "bold"), fg = RED , bg = YELLOW)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 32, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = (window.after(1000, count_down,count-1))
    else:
        start_timer()
        mark =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
            check_mark.config(text=mark)

    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112,image =tomato_img)
timer_text = canvas.create_text(100,130, text ="00:00", font =("Arial", 24, "bold"), fill = "white")
canvas.grid(column = 1 , row= 1)

#Label Timer

timer_label =Label(text = "Timer", font = (FONT_NAME, 32, "bold"), fg = GREEN , bg = YELLOW)
timer_label.grid(column = 1, row = 0)

#Start Button
start_button = Button(text="Start", highlightthickness=0, command= start_timer)
start_button.grid(column = 0, row =2)

#Reset Button
reset_button = Button(text = "Reset", highlightthickness=0, command=reset)
reset_button.grid(column = 2, row =2)

#check mark
check_mark = Label(text="",bg =YELLOW, fg=GREEN, font=("Arial", 21))
check_mark.grid(column=1, row=3)

window.mainloop()