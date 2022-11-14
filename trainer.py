import time
from tkinter import *


class App(Menu):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.text = getattr(parent, "text")
        self.len = len(self.text)
        self.mistakes = 0
        self.timer = 0
        self.start_time = 0
        self.ind = 0
        self.flag_exit = False

        self.window = getattr(parent, "menu")
        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        self.frame3 = Frame(self.window)
        self.frame1.pack()
        self.frame2.pack(side="left")
        self.frame3.pack(side="right")

        self.text_label = Label(self.frame1,
                                text=self.text,
                                bg="gray",
                                width=25,
                                height=5,
                                font=("Times New Roman", 50),
                                anchor="w")
        self.time_label = Label(self.frame2,
                                text="Time: 0.00",
                                bg="blue",
                                width=11,
                                height=1,
                                font=("Times New Roman", 45),
                                anchor="w")
        self.mistakes_label = Label(self.frame3,
                                    text="Mistakes: 0",
                                    bg="blue",
                                    width=12,
                                    height=1,
                                    font=("Times New Roman", 45),
                                    anchor="w")
        self.text_label.pack()
        self.time_label.pack()
        self.mistakes_label.pack()

    def input_key(self, key):
        if self.ind == 0 and self.mistakes == 0:
            self.start_time = time.time()
            self.timer = time.time()
            self.window.after(20, self.display_timer)
        if len(key.char) == 1 and ord(' ') <= ord(key.char) <= ord('~'):
            if key.char != self.text[self.ind]:
                self.mistakes += 1
                self.mistakes_label.destroy()
                self.mistakes_label = Label(self.frame3,
                                            text=f"Mistakes: {self.mistakes}",
                                            bg="blue",
                                            width=12,
                                            height=1,
                                            font=("Times New Roman", 45),
                                            anchor="w")
                self.mistakes_label.pack()
                return
            self.ind += 1
            self.text_label.destroy()
            self.text_label = Label(self.frame1,
                                    text=self.text[self.ind:],
                                    bg="gray",
                                    width=25,
                                    height=5,
                                    font=("Times New Roman", 50),
                                    anchor="w")
            self.text_label.pack()
        if self.ind == self.len:
            self.exit()

    def display_timer(self):
        self.time_label.destroy()
        if self.flag_exit:
            return
        self.timer = time.time()
        timer = str(self.timer - self.start_time).split('.')
        self.time_label = Label(self.frame2,
                                text=f"Time: {timer[0]}.{timer[1][:2]}",
                                bg="blue",
                                width=11,
                                height=1,
                                font=("Times New Roman", 45),
                                anchor="w")
        self.time_label.pack()
        self.window.after(20, self.display_timer)

    def run(self):
        self.window.bind("<KeyPress>", self.input_key)

    def exit(self):
        self.flag_exit = True
        setattr(self.parent, "mistakes", self.mistakes)
        timer = self.timer - self.start_time
        setattr(self.parent, "timer", timer)
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.window.unbind("<KeyPress>")
