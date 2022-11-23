from tkinter import filedialog
from tkinter import Label
from trainer import App


class Menu(App):
    def __init__(self):
        super().__init__(self.statistics,
                         self.load_text,
                         self.train,
                         self.hide_stats,
                         self.show_menu)
        self.build_menu()
        self.window.mainloop()

    def build_menu(self):
        self.window.geometry("750x450+350+200")
        self.play_btn.pack(pady=60)
        self.stats_btn.pack()
        self.load_text_btn.pack(pady=60)

    def hide_menu(self):
        self.play_btn.pack_forget()
        self.stats_btn.pack_forget()
        self.load_text_btn.pack_forget()
        self.window.update()

    def show_menu(self):
        self.play_btn.pack(pady=60)
        self.stats_btn.pack()
        self.load_text_btn.pack(pady=60)
        self.window.update()

    def hide_stats(self):
        self.stats_label.pack_forget()
        self.exit_stats_btn.pack_forget()
        self.show_menu()

    def show_stats(self):
        lpm = str(self.len * 60 / self.timer).split('.')
        str_timer = str(self.timer).split('.')
        self.stats_label = Label(self.window,
                                 text=f"Time: {str_timer[0]}.{str_timer[1][:2]}\n"
                                      f"Mistakes: {self.mistakes}\n"
                                      f"Letters per minute: {lpm[0]}.{lpm[1][:2]}\n",
                                 width=20,
                                 height=5,
                                 font=("Times New Roman", 30))
        self.stats_label.pack()
        self.exit_stats_btn.pack()

    def statistics(self):
        if self.timer == -1:
            return
        self.hide_menu()
        self.show_stats()

    def train(self):
        if self.len == 0:
            return
        self.hide_menu()
        self.build_game()

    def load_text(self):
        file_name = filedialog.askopenfilename(filetypes=(("TXT files", "*.txt"),))
        with open(file_name) as file:
            self.text = ' '.join(file.read().split())
            self.len = len(self.text)


window = Menu()
