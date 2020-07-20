
import tkinter as tk
import pyautogui


win = tk.Tk()
win.title("Take Screenshot")


def takescreenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(r'c:\Users\sajina\Desktop\Screenshot.png')

button = tk.Button(win,text="Capture Screenshot",command=takescreenshot)
button.pack()


win.mainloop()
