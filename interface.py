import tkinter as tk
import time

start_time = 0
running = False
elapsed_time = 0


def update_time(label):
    if running:
        current_time = elapsed_time + (time.time() - start_time)
        hours, remainder = divmod(int(current_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int((current_time - int(current_time)) * 100)
        label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}")
    label.after(100, update_time, label)


def start_timer():
    global start_time, running
    if not running:
        start_time = time.time()
        running = True


def stop_timer():
    global running, elapsed_time
    if running:
        elapsed_time += time.time() - start_time
        running = False


def reset_timer(label):
    global running, elapsed_time
    running = False
    elapsed_time = 0
    label.config(text="00:00:00.00")


def create_interface(root):
    frame = tk.Frame(root)
    frame.pack()

    time_label = tk.Label(frame, font=("Helvetica", 24))
    time_label.pack()

    update_time(time_label)

    start_button = tk.Button(frame, text="Start", command=start_timer)
    start_button.pack(side=tk.LEFT)

    stop_button = tk.Button(frame, text="Stop", command=stop_timer)
    stop_button.pack(side=tk.LEFT)

    reset_button = tk.Button(frame, text="Reset", command=lambda: reset_timer(time_label))
    reset_button.pack(side=tk.LEFT)
