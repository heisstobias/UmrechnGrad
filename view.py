import tkinter as tk



class View:
    def __init__(self):

        self.listener = None

        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("C/F-Umrechnung")

        self.text_c = tk.StringVar()
        self.text_f = tk.StringVar()

        self.heading = tk.Label(self.window, text="Celsius/Fahrenheit Umrechnung", font="Calibri 11 bold")
        self.heading.grid(row=0, column=0, columnspan=2)

        self.entry = tk.Scale(self.window, command=lambda event: self.change(), from_=-200, to=200, orient=tk.HORIZONTAL)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E)

        self.celsius = tk.Label(self.window, font="Calibri 9 bold", textvariable=self.text_c)
        self.celsius.grid(row=2, column=0)

        self.fahrenheit = tk.Label(self.window, font="Calibri 9 bold", textvariable=self.text_f)
        self.fahrenheit.grid(row=2, column=1)


    def set_listener(self, listener):
        self.listener = listener

    def change(self):
        if self.listener:
            self.listener(self.value)



    @property
    def value(self):
        return self.entry.get()

    def set_values(self, celsius, fahrenheit):
        self.text_c.set("{:.2f}° F ist\n {:.2f}° C".format(self.value, celsius))
        self.text_f.set("{:.2f}° C ist\n {:.2f}° F".format(self.value, fahrenheit))

    def show(self):
        self.window.mainloop()