import tkinter as tk
from interface import create_interface

def main():
    root = tk.Tk()
    root.title("Simple Timer")
    root.geometry("200x100")
    root.attributes("-topmost", True)
    #root.iconbitmap("")
    create_interface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
