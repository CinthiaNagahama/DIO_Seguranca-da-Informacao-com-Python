import webbrowser


import webbrowser
from tkinter import *

root = Tk()

root.title("Abrir Browser")
root.geometry("300x200")

def google():
  webbrowser.open("www.google.com")

if __name__ == "__main__":
  mygoogle = Button(root, text="Abrir Google", command=google).pack(pady=20)
  root.mainloop()
