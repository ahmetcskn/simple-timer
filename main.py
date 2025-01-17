import tkinter as tk
from interface import create_interface

def main():
    root = tk.Tk()
    root.title("Simple Timer")
    root.geometry("200x100")
    root.attributes("-topmost", True)
    root.iconbitmap("C:/Users/ahmet/Desktop/simple-timer/icon/1651629.ico")
    create_interface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
