from tkinter import *
from tkinter import filedialog
from trainer import App


class Menu:
    def __init__(self):
        self.text = "abacaba"
        self.len = len(self.text)
        self.timer = -1
        self.mistakes = 0
        self.menu = Tk()
        self.menu.title("Keyboard Trainer")
        self.play_btn = Button(self.menu,
                               text="PLAY",
                               command=self.train,
                               bg="gray",
                               width=20,
                               height=2,
                               font=("Times New Roman", 15))
        self.stats_btn = Button(self.menu,
                                text="Statistic",
                                command=self.statistics,
                                bg="gray",
                                width=20,
                                height=2,
                                font=("Times New Roman", 15))
        self.load_text_btn = Button(self.menu,
                                    text="Load Text From File",
                                    command=self.load_text,
                                    bg="gray",
                                    width=20,
                                    height=2,
                                    font=("Times New Roman", 15))
        self.exit_stats_btn = Button(self.menu,
                                     text="Return to Menu",
                                     command=self.hide_stats,
                                     bg="gray",
                                     width=20,
                                     height=2,
                                     font=("Times New Roman", 15))
        self.stats_label = Label()
        self.build_menu()

    def build_menu(self):
        self.menu.geometry("750x450+350+200")
        self.play_btn.pack(pady=60)
        self.stats_btn.pack()
        self.load_text_btn.pack(pady=60)
        self.menu.mainloop()

    def hide_menu(self):
        self.play_btn.pack_forget()
        self.stats_btn.pack_forget()
        self.load_text_btn.pack_forget()
        self.menu.update()

    def show_menu(self):
        self.play_btn.pack(pady=60)
        self.stats_btn.pack()
        self.load_text_btn.pack(pady=60)
        self.menu.update()

    def hide_stats(self):
        self.stats_label.pack_forget()
        self.exit_stats_btn.pack_forget()
        self.show_menu()

    def show_stats(self):
        lpm = str(self.len * 60 / self.timer).split('.')
        str_timer = str(self.timer).split('.')
        self.stats_label = Label(self.menu,
                                 text=f"Time: {str_timer[0]}.{str_timer[1][:2]}\n"
                                      f"Mistakes: {self.mistakes}\n"
                                      f"Letters per minute: {lpm[0]}.{lpm[1][:2]}\n",
                                 width=20,
                                 height=5,
                                 font=("Times New Roman", 30))
        self.stats_label.pack()
        self.exit_stats_btn.pack()

    def train(self):
        if self.len == 0:
            return
        self.hide_menu()
        trainer = App(self)
        trainer.run()
        self.show_menu()

    def statistics(self):
        if self.timer == -1:
            return
        self.hide_menu()
        self.show_stats()

    def load_text(self):
        file_name = filedialog.askopenfilename(filetypes=(("TXT files", "*.txt"),))
        with open(file_name) as file:
            self.text = ' '.join(file.read().split())
            self.len = len(self.text)


a = Menu()
