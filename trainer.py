import time
from tkinter import Tk, Label, Frame, Button


class App:
    def __init__(self,
                 statistics, load_text, train,
                 hide_stats, show_menu):
        self.text = "abacaba"
        self.len = len(self.text)
        self.start_time = 0
        self.status = "menu"
        self.ind = 0
        self.timer = -1
        self.mistakes = 0
        self.flag_exit = False

        self.window = Tk()
        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        self.frame3 = Frame(self.window)
        self.window.title("Keyboard Trainer")
        self.window.resizable(width=False, height=False)
        self.show_menu = show_menu

        self.stats_btn = Button(self.window,
                                text="Statistic",
                                command=statistics,
                                bg="gray",
                                width=20,
                                height=2,
                                font=("Times New Roman", 15))
        self.load_text_btn = Button(self.window,
                                    text="Load Text From File",
                                    command=load_text,
                                    bg="gray",
                                    width=20,
                                    height=2,
                                    font=("Times New Roman", 15))
        self.exit_stats_btn = Button(self.window,
                                     text="Return to Menu",
                                     command=hide_stats,
                                     bg="gray",
                                     width=20,
                                     height=2,
                                     font=("Times New Roman", 15))
        self.play_btn = Button(self.window,
                               text="PLAY",
                               command=train,
                               bg="gray",
                               width=20,
                               height=2,
                               font=("Times New Roman", 15))
        self.stats_label = Label()
        self.time_label = Label()
        self.text_label = Label()
        self.mistakes_label = Label()

    def build_game(self):
        self.text_label = Label(self.frame1,
                                text=self.text,
                                width=25,
                                height=5,
                                font=("Times New Roman", 50),
                                anchor="w")
        self.time_label = Label(self.frame2,
                                text="Time: 0.00",
                                width=11,
                                height=1,
                                font=("Times New Roman", 45),
                                anchor="w")
        self.mistakes_label = Label(self.frame3,
                                    text="Mistakes: 0",
                                    width=12,
                                    height=1,
                                    font=("Times New Roman", 45),
                                    anchor="w")
        self.flag_exit = False
        self.status = "game"
        self.ind = 0
        self.mistakes = 0
        self.timer = 0
        self.start_time = time.time()
        self.frame1.pack()
        self.frame2.pack(side="left")
        self.frame3.pack(side="right")
        self.text_label.pack()
        self.time_label.pack()
        self.mistakes_label.pack()
        self.window.bind("<KeyPress>", self.input_key)

    def exit(self):
        self.status = "menu"
        self.flag_exit = True
        self.text_label.pack_forget()
        self.time_label.pack_forget()
        self.mistakes_label.pack_forget()
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.timer = self.timer - self.start_time
        self.window.unbind("<KeyPress>")
        self.show_menu()

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
                                width=11,
                                height=1,
                                font=("Times New Roman", 45),
                                anchor="w")
        self.time_label.pack()
        self.window.after(50, self.display_timer)
