import tkinter as tk
import time
import threading
import random

class Viteza:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SpeedTypingGame")
        self.root.geometry("800x600")
        self.root.configure(bg="green")

        self.frazeposibile = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root, bg="green")
        self.sample_label = tk.Label(self.frame, text=random.choice(self.frazeposibile), font=("Helvetica", 18), bg="green")
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24), bg="light green")
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)

        self.speed_label = tk.Label(self.frame, text="Viteza: \n0.00 Caractere pe secunda\n0.00 Caractere pe minut", font=("Helvetica", 18), bg="green")
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)
        self.counter = 0
        self.running = False
        self.finished_correctly = False
        self.mainloop()

    def start(self, event):
        if not self.finished_correctly:
            if not self.running:
                if event.keycode not in [16, 17, 18]:
                    self.running = True
                    t = threading.Thread(target=self.time_thread)
                    t.start()

            if self.sample_label.cget('text') != self.input_entry.get():
                self.input_entry.config(fg="red")
            else:
                self.input_entry.config(fg="black")
                if self.input_entry.get() == self.sample_label.cget('text'):
                    self.finished_correctly = True
                    self.running = False
                    self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cpers = len(self.input_entry.get()) / self.counter
            cperm = cpers * 60
            self.speed_label.config(text=f"Viteza: \n{cpers:.2f} Caractere pe secunda\n{cperm:.2f} Caractere pe minut")

    def reset(self):
        self.finished_correctly = False
        self.running = False
        self.sample_label.config(text=random.choice(self.frazeposibile))
        self.input_entry.delete(0, tk.END)
        self.speed_label.config(text="Viteza: \n0.00 Caractere pe secunda\n0.00 Caractere pe minut")

    def mainloop(self):
        self.root.mainloop()

Viteza()




